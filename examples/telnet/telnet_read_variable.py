"""
Telnet - Read Variable
======================
Read any robot variable via Telnet KCL.
The user chooses which variable to read (e.g. $MCR.$GENOVERRIDE, $CUSTOM, ...).

Variables follow FANUC naming: $VARIABLE_NAME or $GROUP.$MEMBER
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Telnet: Read Variable")
print("=" * 60)

# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

try:
    while True:
        # Ask user which variable to read
        var_name = input("Enter variable name to read (e.g. $MCR.$GENOVERRIDE) [q to quit]: ").strip()
        if var_name.lower() == 'q':
            break
        if not var_name:
            print("Variable name cannot be empty.")
            continue

        # Read the variable
        result = robot.telnet.get_variable(var_name)

        if result.succeed:
            print(f"  {var_name} = {result.raw_value}")
        else:
            print(f"  Error: {result.error_text}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
