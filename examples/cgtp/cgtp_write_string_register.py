"""
CGTP - Write String Register
==============================
Write a string value to a string register SR[index].
Uses write_string_register().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Write String Register")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    idx_str = input("Register index (e.g. 1 for SR[1]): ").strip()
    idx = int(idx_str)

    value = input("String value to write: ").strip()

    robot.cgtp.write_string_register(idx, value)
    print(f"\n  SR[{idx}] written: '{value}'")

finally:
    robot.disconnect()
    print("\nDisconnected.")
