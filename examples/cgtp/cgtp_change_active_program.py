"""
CGTP - Change Active Program
==============================
Change the active TP program on the controller.
Uses change_active_program().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Change Active Program")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    prog = input("Program name to activate: ").strip()
    if not prog:
        print("No name provided.")
    else:
        print(f"Changing active program to '{prog}'...")
        robot.cgtp.change_active_program(prog)
        print("Active program changed.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
