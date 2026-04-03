"""
CGTP - Rename Program
======================
Rename a TP program on the controller.
Uses rename_program().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Rename Program")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    source = input("Current program name: ").strip()
    new_name = input("New program name: ").strip()

    if not source or not new_name:
        print("Both names are required.")
    else:
        print(f"\nRenaming '{source}' to '{new_name}'...")
        robot.cgtp.rename_program(source, new_name)
        print("Program renamed successfully.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
