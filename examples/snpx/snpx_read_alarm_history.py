"""
SNPX - Read Alarm History
===========================
Read the alarm history from the robot via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Alarm History")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    count_str = input("How many alarm history entries to read (default 10): ").strip()
    count = int(count_str) if count_str else 10

    print(f"\nAlarm History (last {count} entries):")
    print("-" * 70)

    for i in range(1, count + 1):
        try:
            alarm = robot.snpx.alarm_history.read(i)
            if alarm and alarm.message:
                print(f"  [{i:3d}] {alarm.severity_message:<10} | {alarm.message}")
                if alarm.cause_message:
                    print(f"        Cause: {alarm.cause_message}")
        except Exception:
            break

finally:
    robot.disconnect()
    print("\nDisconnected.")
