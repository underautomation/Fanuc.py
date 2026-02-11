"""
SNPX - Write Numeric Register
===============================
Write a value to a numeric register (R[i]) via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Write Numeric Register")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    while True:
        reg_str = input("Enter register number to write (e.g. 1 for R[1]) [q to quit]: ").strip()
        if reg_str.lower() == 'q':
            break

        try:
            reg_num = int(reg_str)
        except ValueError:
            print("  Invalid number.")
            continue

        value_str = input(f"Enter new value for R[{reg_num}]: ").strip()
        try:
            value = float(value_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read current value first
        old_value = robot.snpx.numeric_registers.read(reg_num)

        # Write new value
        robot.snpx.numeric_registers.write(reg_num, value)

        # Read back to confirm
        new_value = robot.snpx.numeric_registers.read(reg_num)
        print(f"  R[{reg_num}]: {old_value} -> {new_value}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
