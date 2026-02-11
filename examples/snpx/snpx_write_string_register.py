"""
SNPX - Write String Register
==============================
Write a string value to a string register (SR[i]) via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Write String Register")
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

        # Read current value
        old_value = robot.snpx.string_registers.read(sr_num)
        print(f"  Current SR[{sr_num}] = \"{old_value}\"")

        new_value = input(f"  Enter new string value: ").strip()

        # Write new value
        robot.snpx.string_registers.write(sr_num, new_value)

        # Read back to confirm
        confirm = robot.snpx.string_registers.read(sr_num)
        print(f"  SR[{sr_num}]: \"{old_value}\" -> \"{confirm}\"")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
