"""
SNPX - Write System Variable
==============================
Write a value to a system variable via SNPX protocol.
Uses the set_variable method for flexible variable access.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Write System Variable")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    print("\nExample variables you can write:")
    print("  $MCR.$GENOVERRIDE    - Speed override (0-100)")

    while True:
        var_name = input("\nEnter variable name [q to quit]: ").strip()
        if var_name.lower() == 'q':
            break
        if not var_name:
            continue

        value_str = input(f"Enter new value for {var_name}: ").strip()

        try:
            robot.snpx.set_variable(var_name, value_str)
            print(f"  {var_name} set to {value_str}")
        except Exception as e:
            print(f"  Error: {e}")
finally:
    robot.disconnect()
    print("Disconnected.")
