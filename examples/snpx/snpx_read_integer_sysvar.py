"""
SNPX - Read System Variable (Integer)
=======================================
Read an integer system variable by name via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Integer System Variable")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    print("\nExamples of integer system variables:")
    print("  $MCR.$GENOVERRIDE   - Speed override percentage")
    print("  $SCR.$NUM_GROUP     - Number of motion groups")
    print("  $TIMER[1].$TIMER_VAL - Timer 1 value")
    print("  $RMT_MASTER - Remote master")

    while True:
        var_name = input("\nEnter variable name [q to quit]: ").strip()
        if var_name.lower() == 'q':
            break
        if not var_name:
            continue

        try:
            value = robot.snpx.integer_system_variables.read(var_name)
            print(f"  {var_name} = {value}")
        except Exception as e:
            print(f"  Error: {e}")
finally:
    robot.disconnect()
    print("Disconnected.")
