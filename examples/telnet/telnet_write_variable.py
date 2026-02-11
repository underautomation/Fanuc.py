"""
Telnet - Write Variable
=======================
Write a numeric value to any robot variable via Telnet KCL.
The user chooses the variable name and the new value.

Shows the former value and new value after writing.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Telnet: Write Variable")
print("=" * 60)

# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

try:
    while True:
        var_name = input("Enter variable name to write (e.g. $MCR.$GENOVERRIDE) [q to quit]: ").strip()
        if var_name.lower() == 'q':
            break
        if not var_name:
            continue

        value_str = input(f"Enter new value for {var_name}: ").strip()
        try:
            value = float(value_str)
        except ValueError:
            print("  Invalid number. Please enter a numeric value.")
            continue

        # Write the variable
        result = robot.telnet.set_variable(var_name, value)

        if result.succeed:
            print(f"  Success! {var_name}: {result.former_value} -> {result.new_value}")
        else:
            print(f"  Error: {result.error_text}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
