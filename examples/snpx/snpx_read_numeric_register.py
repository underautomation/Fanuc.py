"""
SNPX - Read Numeric Register
==============================
Read a numeric register (R[i]) from the robot via SNPX protocol.
SNPX provides direct, fast access to robot data.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Numeric Register")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    while True:
        reg_str = input("Enter register number to read (e.g. 1 for R[1]) [q to quit]: ").strip()
        if reg_str.lower() == 'q':
            break

        try:
            reg_num = int(reg_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read numeric register via SNPX
        value = robot.snpx.numeric_registers.read(reg_num)
        print(f"  R[{reg_num}] = {value}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
