"""
SNPX - Clear Alarms
=====================
Clear all active alarms on the robot via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Clear Alarms")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    # First show active alarms
    print("Checking for active alarms...")
    try:
        alarm = robot.snpx.active_alarm.read(1)
        if alarm and alarm.message:
            print(f"  Active alarm: {alarm.message}")
        else:
            print("  No active alarms.")
    except:
        print("  No active alarms.")

    confirm = input("\nClear all alarms? (y/n): ").strip().lower()
    if confirm == 'y':
        robot.snpx.clear_alarms()
        print("  Alarms cleared.")
    else:
        print("  Cancelled.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
