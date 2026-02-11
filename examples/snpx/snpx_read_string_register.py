"""
SNPX - Read String Register
=============================
Read a string register (SR[i]) from the robot via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read String Register")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    while True:
        sr_str = input("Enter string register number (e.g. 1 for SR[1]) [q to quit]: ").strip()
        if sr_str.lower() == 'q':
            break

        try:
            sr_num = int(sr_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read string register via SNPX
        value = robot.snpx.string_registers.read(sr_num)
        print(f"  SR[{sr_num}] = \"{value}\"")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
