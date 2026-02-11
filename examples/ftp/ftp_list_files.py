"""
FTP - List Files on Controller
================================
Browse files and directories on the robot controller's file system via FTP.
The user can navigate through directories.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: List Files on Controller")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    current_path = "/md:/"

    while True:
        print(f"\nListing: {current_path}")
        print("-" * 60)

        items = robot.ftp.direct_file_handling.get_listing(current_path)

        print(f"  {'#':>3}  {'Type':<5} {'Name':<30} {'Size':<15} {'Modified':<20}")
        print(f"  {'---':>3}  {'-----':<5} {'-----':<30} {'-----':<15} {'-----':<20}")

        for i, item in enumerate(items):
            type_str = "[DIR]" if str(item.type) == "Directory" else "     "
            size_str = f"{item.size} bytes" if item.size > 0 else ""
            modified_str = item.modified.strftime("%Y-%m-%d") if item.modified.year > 1 else ""
            print(f"  {i+1:3}. {type_str} {item.name:<30} {size_str:<15} {modified_str:<20}")

        print()
        user_input = input("Enter path to browse, '..' to go up, or 'q' to quit: ").strip()
        if user_input.lower() == 'q':
            break
        elif user_input == '..':
            # Go up one level
            parts = current_path.rstrip('/').rsplit('/', 1)
            current_path = parts[0] if parts[0] else "/"
        elif user_input:
            # Navigate to subdirectory
            if not user_input.startswith('/'):
                current_path = current_path.rstrip('/') + '/' + user_input
            else:
                current_path = user_input

finally:
    robot.disconnect()
    print("Disconnected.")
