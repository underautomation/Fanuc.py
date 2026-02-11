"""
FANUC SDK - Interactive Example Launcher
==========================================
Browse and run all SDK examples from a single interactive menu.
Examples are discovered dynamically from subdirectories.
"""
import os
import sys
import ast
import runpy
import unicodedata
from pathlib import Path

# ─── Constants ────────────────────────────────────────────────────────────────
EXAMPLES_DIR = Path(__file__).parent
IGNORED_FILES = {"__init__.py", "launcher.py"}
CATEGORY_ICONS = {
    "ftp":        "📂",
    "kinematics": "🦾",
    "snpx":       "⚡",
    "telnet":     "🔌",
    "license":    "🔑",
}
CATEGORY_DESCRIPTIONS = {
    "ftp":        "File Transfer Protocol - read/write files, registers, diagnostics",
    "kinematics": "Kinematics - offline forward & inverse kinematics, no connection needed",
    "snpx":       "SNPX industrial protocol - fast real-time register & I/O access",
    "telnet":     "Telnet KCL - send commands, read variables, control I/O",
    "license":    "License management - activation & status",
}

# ─── Box-drawing helpers ─────────────────────────────────────────────────────
WIDTH = 80

def _display_width(text):
    """Compute the visual width of *text* in a terminal, accounting for wide / emoji chars."""
    width = 0
    for ch in text:
        cp = ord(ch)
        eaw = unicodedata.east_asian_width(ch)
        if eaw in ('F', 'W'):
            width += 2
        elif cp >= 0x1F000:          # supplementary-plane emoji
            width += 2
        elif 0x2600 <= cp <= 0x27BF: # misc symbols & dingbats (⚡ …)
            width += 2
        elif 0xFE00 <= cp <= 0xFE0F: # variation selectors
            width += 0
        else:
            width += 1
    return width

def box_top():    print("╔" + "═" * WIDTH + "╗")
def box_bot():    print("╚" + "═" * WIDTH + "╝")
def box_sep():    print("╠" + "═" * WIDTH + "╣")
def box_line(text="", align="<"):
    dw = _display_width(text)
    pad = max(0, WIDTH - dw)
    if align == "^":
        left_pad = pad // 2
        right_pad = pad - left_pad
        inner = " " * left_pad + text + " " * right_pad
    elif align == ">":
        inner = " " * pad + text
    else:
        inner = text + " " * pad
    print(f"║{inner}║")

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ─── Discovery ───────────────────────────────────────────────────────────────
def extract_docstring(filepath: Path) -> str:
    """Extract the module-level docstring from a Python file using AST."""
    try:
        source = filepath.read_text(encoding="utf-8")
        tree = ast.parse(source)
        docstring = ast.get_docstring(tree)
        return docstring if docstring else "(no description)"
    except Exception:
        return "(could not parse file)"


def parse_docstring(raw: str):
    """
    Split a docstring like:
        Title
        =====
        Description line 1
        Description line 2
    into (title, description).
    """
    lines = raw.strip().splitlines()
    title = lines[0].strip() if lines else "Untitled"
    # Skip the RST underline (===)
    desc_lines = []
    skipped_underline = False
    for line in lines[1:]:
        stripped = line.strip()
        if not skipped_underline and set(stripped) <= {"=", "-", "~"} and stripped:
            skipped_underline = True
            continue
        if stripped:
            desc_lines.append(stripped)
    description = " ".join(desc_lines) if desc_lines else ""
    return title, description


def discover_examples():
    """
    Walk subdirectories of examples/ and return a dict:
        { category_name: [ (title, description, Path), ... ] }
    sorted alphabetically within each category.
    """
    categories = {}
    for subdir in sorted(EXAMPLES_DIR.iterdir()):
        if not subdir.is_dir() or subdir.name.startswith("_"):
            continue
        examples = []
        for py_file in sorted(subdir.glob("*.py")):
            if py_file.name in IGNORED_FILES:
                continue
            raw = extract_docstring(py_file)
            title, description = parse_docstring(raw)
            examples.append((title, description, py_file))
        if examples:
            categories[subdir.name] = examples
    return categories


# ─── Rendering ────────────────────────────────────────────────────────────────
def render_banner():
    box_top()
    box_line()
    box_line("  ███████╗ █████╗ ███╗   ██╗██╗   ██╗ ██████╗", "^")
    box_line("  ██╔════╝██╔══██╗████╗  ██║██║   ██║██╔════╝", "^")
    box_line("  █████╗  ███████║██╔██╗ ██║██║   ██║██║     ", "^")
    box_line("  ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║██║     ", "^")
    box_line("  ██║     ██║  ██║██║ ╚████║╚██████╔╝╚██████╗", "^")
    box_line("  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝", "^")
    box_line()
    box_line("  Python SDK - Interactive Example Launcher", "^")
    box_line()
    box_bot()


def render_category_menu(categories):
    """Show top-level category selection."""
    box_top()
    box_line("  SELECT A CATEGORY", "^")
    box_sep()
    box_line()
    cat_list = list(categories.keys())
    for idx, cat_name in enumerate(cat_list, 1):
        icon = CATEGORY_ICONS.get(cat_name, "📁")
        count = len(categories[cat_name])
        label = f"  {icon}  {idx}. {cat_name.upper():<12} ({count} example{'s' if count != 1 else ''})"
        box_line(label)
        desc = CATEGORY_DESCRIPTIONS.get(cat_name, "")
        if desc:
            box_line(f"         {desc}")
        box_line()
    box_sep()
    box_line("  0. Exit")
    box_line()
    box_bot()
    return cat_list


def render_example_list(cat_name, examples):
    """Show examples within a category with descriptions."""
    icon = CATEGORY_ICONS.get(cat_name, "📁")
    clear()
    box_top()
    box_line(f"  {icon}  {cat_name.upper()} EXAMPLES", "^")
    box_sep()

    for idx, (title, description, _path) in enumerate(examples, 1):
        box_line()
        # Number + title
        num = f"  {idx:>2}."
        box_line(f"{num} {title}")
        # Description, word-wrapped to fit
        if description:
            max_desc = WIDTH - 8
            words = description.split()
            line = ""
            for w in words:
                if len(line) + len(w) + 1 > max_desc:
                    box_line(f"      {line}")
                    line = w
                else:
                    line = f"{line} {w}" if line else w
            if line:
                box_line(f"      {line}")

    box_line()
    box_sep()
    box_line("  0. ← Back to categories")
    box_line()
    box_bot()


def render_running_header(title, filepath):
    print()
    box_top()
    box_line(f"  ▶ Running: {title}")
    box_line(f"    {filepath}")
    box_bot()
    print()


# ─── Input helpers ────────────────────────────────────────────────────────────
def prompt_choice(prompt_text, max_val):
    """Ask for an integer in [0, max_val]. Returns int or None on bad input."""
    try:
        text = input(prompt_text).strip()
        val = int(text)
        if 0 <= val <= max_val:
            return val
    except (ValueError, EOFError):
        pass
    return None


def pause():
    print()
    input("  Press Enter to return to the menu...")


# ─── Run example ──────────────────────────────────────────────────────────────
def run_example(title, filepath: Path):
    """Run an example in-process so the VS Code debugger can step into it."""
    render_running_header(title, filepath.relative_to(EXAMPLES_DIR.parent))
    try:
        # Run in the same process - breakpoints in example files will work
        runpy.run_path(str(filepath), run_name="__main__")
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print("\n  (interrupted)")
    except Exception as exc:
        print(f"\n  Error: {exc}")
    pause()


# ─── Main loop ────────────────────────────────────────────────────────────────
def main():
    categories = discover_examples()
    if not categories:
        print("No examples found in subdirectories of", EXAMPLES_DIR)
        return

    while True:
        clear()
        render_banner()
        print()
        cat_list = render_category_menu(categories)
        print()
        choice = prompt_choice(f"  Enter category number [0-{len(cat_list)}]: ", len(cat_list))

        if choice is None:
            continue
        if choice == 0:
            clear()
            print("  Goodbye!\n")
            break

        cat_name = cat_list[choice - 1]
        examples = categories[cat_name]

        # Example sub-menu loop
        while True:
            render_example_list(cat_name, examples)
            print()
            ex_choice = prompt_choice(
                f"  Enter example number [0-{len(examples)}]: ", len(examples)
            )
            if ex_choice is None:
                continue
            if ex_choice == 0:
                break

            title, _desc, filepath = examples[ex_choice - 1]
            clear()
            run_example(title, filepath)


if __name__ == "__main__":
    main()
