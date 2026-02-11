"""
FTP - Interactive Variable Navigator
======================================
Browse all variable files on the robot controller via FTP.
Provides an interactive console to navigate through variable files,
inspect variables, and drill into structured/array fields.

Navigation:
  - Select a variable file to explore its contents
  - Browse variables with pagination
  - Drill into structured variables to see sub-fields
  - Search variables by name or value
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.ftp.variables.value_kind import ValueKind

# ==============================================================================
# Display helpers
# ==============================================================================
PAGE_SIZE = 20

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print()
    print("=" * 64)
    print(f"  {title}")
    print("=" * 64)

def print_separator():
    print("-" * 64)

def prompt(text="Your choice"):
    """Prompt user for input and return stripped string."""
    try:
        return input(f"\n{text}: ").strip()
    except (EOFError, KeyboardInterrupt):
        return "q"

def kind_label(kind):
    """Return a human-readable label for a ValueKind."""
    if kind == ValueKind.Value:
        return "Value"
    elif kind == ValueKind.Array:
        return "Array"
    elif kind == ValueKind.Structure:
        return "Struct"
    elif kind == ValueKind.File:
        return "File"
    return str(kind)

def format_value(var):
    """Format a variable's value for display, handling uninitialized and long strings."""
    if var.is_uninitialized:
        return "(uninitialized)"
    val = var.value
    if val is None:
        return ""
    if len(str(val)) > 50:
        return str(val)[:47] + "..."
    return str(val)


# ==============================================================================
# Level 3: Inspect a single variable in detail (with sub-fields)
# ==============================================================================
def inspect_variable(var, breadcrumb=""):
    """Display full details of a variable and let the user drill into sub-fields."""
    while True:
        clear_screen()
        print_header(f"Variable Detail")
        if breadcrumb:
            print(f"  Path: {breadcrumb}")

        print(f"\n  Name           : {var.name}")
        print(f"  Full name      : {var.full_name}")
        print(f"  Kind           : {kind_label(var.kind)}")
        print(f"  Register name  : {var.register_name or '-'}")
        print(f"  Uninitialized  : {var.is_uninitialized}")

        if var.kind == ValueKind.Value or (var.kind != ValueKind.Array and var.kind != ValueKind.Structure):
            print(f"  Value          : {format_value(var)}")

        # Show sub-fields if any
        sub_fields = var.fields
        if sub_fields and len(sub_fields) > 0:
            print(f"\n  Sub-fields ({len(sub_fields)}):")
            print_separator()
            print(f"  {'#':>4}  {'Name':<25} {'Kind':<8} {'Value'}")
            print(f"  {'----':>4}  {'-'*25:<25} {'-'*8:<8} {'-'*20}")
            for i, f in enumerate(sub_fields):
                val_str = format_value(f)
                print(f"  {i+1:4}  {f.name:<25} {kind_label(f.kind):<8} {val_str}")

            print(f"\n  Enter a sub-field number to drill down")
            print(f"  [b] Back")
            choice = prompt()

            if choice.lower() in ('b', 'back', ''):
                return
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(sub_fields):
                    sub = sub_fields[idx]
                    new_crumb = f"{breadcrumb} > {sub.name}" if breadcrumb else sub.name
                    inspect_variable(sub, new_crumb)
        else:
            print(f"\n  No sub-fields.")
            prompt("Press Enter to go back")
            return


# ==============================================================================
# Level 2: Browse variables inside a file (with pagination and search)
# ==============================================================================
def browse_variables(var_file):
    """Paginated browser for all variables in a file."""
    variables = var_file.variables
    total = len(variables)
    page = 0
    search_filter = None

    while True:
        # Apply search filter
        if search_filter:
            filtered = [v for v in variables
                        if search_filter.lower() in (v.name or "").lower()
                        or search_filter.lower() in (v.register_name or "").lower()
                        or search_filter.lower() in str(v.value or "").lower()]
        else:
            filtered = list(variables)

        total_filtered = len(filtered)
        max_page = max(0, (total_filtered - 1) // PAGE_SIZE)
        page = min(page, max_page)

        start = page * PAGE_SIZE
        end = min(start + PAGE_SIZE, total_filtered)
        page_items = filtered[start:end]

        clear_screen()
        print_header(f"Variables in: {var_file.name}")
        print(f"  Total: {total} variables", end="")
        if search_filter:
            print(f"  |  Filter: \"{search_filter}\" ({total_filtered} matches)", end="")
        print(f"  |  Page {page+1}/{max_page+1}")
        print_separator()
        print(f"  {'#':>5}  {'Name':<30} {'Kind':<8} {'Value'}")
        print(f"  {'-----':>5}  {'-'*30:<30} {'-'*8:<8} {'-'*20}")

        for i, var in enumerate(page_items):
            idx = start + i + 1
            label = var.register_name
            display_name = f"{var.name}" if not label else f"{var.name} ({label})"
            if len(display_name) > 30:
                display_name = display_name[:27] + "..."
            val_str = format_value(var)
            print(f"  {idx:5}  {display_name:<30} {kind_label(var.kind):<8} {val_str}")

        print()
        print("  Commands:")
        print("    [number]  Inspect variable         [n] Next page")
        print("    [p] Previous page                   [s] Search / filter")
        print("    [c] Clear filter                    [b] Back to file list")

        choice = prompt()

        if choice.lower() in ('b', 'back'):
            return
        elif choice.lower() == 'n':
            if page < max_page:
                page += 1
        elif choice.lower() == 'p':
            if page > 0:
                page -= 1
        elif choice.lower() == 's':
            search_filter = prompt("Search term (name, comment, or value)")
            page = 0
        elif choice.lower() == 'c':
            search_filter = None
            page = 0
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < total_filtered:
                var = filtered[idx]
                inspect_variable(var, f"{var_file.name} > {var.name}")


# ==============================================================================
# Level 1: File list (top-level menu)
# ==============================================================================
def file_list_menu(all_variables):
    """Main menu: show all variable files and let the user pick one."""
    files = all_variables.fields

    while True:
        clear_screen()
        print_header("FANUC SDK - Variable File Navigator")
        print(f"\n  Available variable files ({len(files)}):\n")
        print(f"  {'#':>4}  {'File Name':<30} {'Variables':>10}")
        print(f"  {'----':>4}  {'-'*30:<30} {'-'*10:>10}")

        for i, vf in enumerate(files):
            var_count = len(vf.variables) if hasattr(vf, 'variables') else "?"
            print(f"  {i+1:4}  {vf.name:<30} {str(var_count):>10}")

        print()
        print("  Commands:")
        print("    [number]  Open variable file")
        print("    [q]       Quit")

        choice = prompt()

        if choice.lower() in ('q', 'quit', 'exit'):
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                browse_variables(files[idx])
            else:
                print(f"  Invalid number. Enter 1-{len(files)}.")


# ==============================================================================
# Main
# ==============================================================================
print("=" * 64)
print("  FANUC SDK - FTP: Interactive Variable Navigator")
print("=" * 64)

robot = connect_robot(enable_ftp=True)

try:
    print("\nLoading all variable files from the controller...")
    print("(This may take a moment)\n")
    all_variables = robot.ftp.get_all_variables()

    file_count = len(all_variables.fields)
    print(f"Loaded {file_count} variable file(s). Starting navigator...\n")

    file_list_menu(all_variables)

    print("\nDone. Thank you for using the Variable Navigator.")

finally:
    robot.disconnect()
    print("Disconnected.")
