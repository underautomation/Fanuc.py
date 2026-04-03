"""
CGTP - Write Numeric Register
===============================
Write an integer or real value to a numeric register R[index].
Uses write_numeric_register_as_integer() and write_numeric_register_as_double().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Write Numeric Register")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    idx_str = input("Register index (e.g. 1 for R[1]): ").strip()
    idx = int(idx_str)

    reg_type = input("Type: (i)nteger or (r)eal [i]: ").strip().lower()
    if not reg_type:
        reg_type = "i"

    value_str = input("Value to write: ").strip()

    if reg_type == "r":
        value = float(value_str)
        robot.cgtp.write_numeric_register_as_double(idx, value)
        print(f"\n  R[{idx}] written as real: {value}")
    else:
        value = int(value_str)
        robot.cgtp.write_numeric_register_as_integer(idx, value)
        print(f"\n  R[{idx}] written as integer: {value}")

    # Verify
    reg = robot.cgtp.read_numeric_register_with_comment(idx)
    print(f"  R[{idx}] read back: {reg}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
