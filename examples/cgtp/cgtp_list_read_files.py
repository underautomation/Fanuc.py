"""
CGTP - List & Read Files
==========================
List files on the controller and read file content as string.
Uses list_files() and get_file_as_string().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: List & Read Files")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    path = input("Path to list (default MD:): ").strip()
    if not path:
        path = "MD:"

    print(f"\nListing files at '{path}'...")
    files = robot.cgtp.list_files(path)
    print(f"Found {len(files)} entries:")
    for f in files:
        print(f"  {f}")

    # Read a file
    file_name = input("\nFile to read as string (leave empty to skip): ").strip()
    if file_name:
        content = robot.cgtp.get_file_as_string(file_name)
        print(f"\nContent of '{file_name}':")
        print("-" * 40)
        # Limit output to avoid flooding
        lines = content.splitlines()
        for line in lines[:50]:
            print(f"  {line}")
        if len(lines) > 50:
            print(f"  ... ({len(lines) - 50} more lines)")

finally:
    robot.disconnect()
    print("\nDisconnected.")
