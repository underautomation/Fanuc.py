"""
CGTP - Write Variable
======================
Write a numeric value to a system or program variable.
Uses write_variable().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Write Variable")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    var_name = input("Variable name (e.g. $MCR.$GENOVERRIDE): ").strip()
    prog = input("Program name (leave empty for system variable): ").strip() or None
    value_str = input("Value to write: ").strip()

    # Read current value
    current = robot.cgtp.read_variable_as_string(var_name, prog)
    print(f"\n  Current value: {current}")

    print(f"  Writing {value_str}...")
    robot.cgtp.write_variable(var_name, value_str, prog)

    # Verify
    new_value = robot.cgtp.read_variable_as_string(var_name, prog)
    print(f"  New value    : {new_value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
