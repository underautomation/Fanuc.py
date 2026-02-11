"""
SNPX - Write Flag
===================
Write a boolean flag (FLG[i]) on the robot via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Write Flag")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    while True:
        flag_str = input("Enter flag number to write (e.g. 1 for FLG[1]) [q to quit]: ").strip()
        if flag_str.lower() == 'q':
            break

        try:
            flag_num = int(flag_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read current value
        old_value = robot.snpx.flags.read(flag_num)
        print(f"  Current FLG[{flag_num}] = {'ON' if old_value else 'OFF'}")

        value_str = input(f"  Enter new value (1=ON, 0=OFF): ").strip()
        try:
            value = bool(int(value_str))
        except ValueError:
            print("  Invalid value.")
            continue

        # Write flag
        robot.snpx.flags.write(flag_num, value)

        # Read back to confirm
        new_value = robot.snpx.flags.read(flag_num)
        print(f"  FLG[{flag_num}]: {'ON' if old_value else 'OFF'} -> {'ON' if new_value else 'OFF'}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
