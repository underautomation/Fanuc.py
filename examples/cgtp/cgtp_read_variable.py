"""
CGTP - Read Variable
=====================
Read a system or program variable as a string or typed value.
Uses read_variable_as_string() and read_variable().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Read Variable")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    while True:
        var_name = input("Variable name (e.g. $MCR.$GENOVERRIDE) [q to quit]: ").strip()
        if var_name.lower() == "q":
            break

        prog = input("Program name (leave empty for system variable): ").strip() or None

        # Read as string
        value_str = robot.cgtp.read_variable_as_string(var_name, prog)
        print(f"  String value: {value_str}")

        # Read as typed value
        value = robot.cgtp.read_variable(var_name, prog)
        print(f"  Type        : {value.type.name}")
        print(f"  Value       : {value.string_value}")
        print()

finally:
    robot.disconnect()
    print("\nDisconnected.")
