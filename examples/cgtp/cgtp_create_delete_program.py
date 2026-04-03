"""
CGTP - Create & Delete Program
================================
Create a new TP program on the controller and optionally delete it.
Uses create_program() and delete_program().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.cgtp_program_sub_type import CgtpProgramSubType

print("=" * 60)
print("  FANUC SDK - CGTP: Create & Delete Program")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    name = input("New program name: ").strip()
    if not name:
        print("No name provided, exiting.")
    else:
        owner = input("Owner (optional): ").strip() or None
        comment = input("Comment (optional): ").strip() or None
        group_str = input("Default motion group (0 to omit, default 0): ").strip()
        group = int(group_str) if group_str else 0

        print(f"\nCreating program '{name}'...")
        robot.cgtp.create_program(name, owner=owner, comment=comment, defaultGroup=group)
        print("Program created successfully.")

        delete = input(f"\nDelete program '{name}'? (y/n) [n]: ").strip().lower()
        if delete == "y":
            robot.cgtp.delete_program(name)
            print("Program deleted.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
