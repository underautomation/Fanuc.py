"""
SNPX - Read Flag
==================
Read a boolean flag (FLG[i]) from the robot via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Flag")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    while True:
        flag_str = input("Enter flag number to read (e.g. 1 for FLG[1]) [q to quit]: ").strip()
        if flag_str.lower() == 'q':
            break

        try:
            flag_num = int(flag_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read flag via SNPX
        value = robot.snpx.flags.read(flag_num)
        state = "ON (True)" if value else "OFF (False)"
        print(f"  FLG[{flag_num}] = {state}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
