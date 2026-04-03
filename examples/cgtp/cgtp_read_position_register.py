"""
CGTP - Read Position Register
===============================
Read a position register PR[index] with its comment and position data.
Uses read_position_register_with_comment().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Read Position Register")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    while True:
        idx_str = input("Position register index (e.g. 1 for PR[1]) [q to quit]: ").strip()
        if idx_str.lower() == "q":
            break

        idx = int(idx_str)
        group_str = input("Motion group (default 1): ").strip()
        group = int(group_str) if group_str else 1

        pr = robot.cgtp.read_position_register_with_comment(idx, group)
        print(f"\n  PR[{idx}] (group {group}):")
        print(f"  Comment : {pr.comment}")
        print(f"  Value   : {pr}")
        print()

finally:
    robot.disconnect()
    print("\nDisconnected.")
