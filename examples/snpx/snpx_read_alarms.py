"""
SNPX - Read Active Alarms
===========================
Read the currently active alarms on the robot via SNPX protocol.
Shows alarm ID, severity, message, and cause.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Active Alarms")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    print("Reading active alarms...")
    
    # Read up to 5 active alarms (indices 1..5)
    count_str = input("How many alarm slots to check (default 5): ").strip()
    count = int(count_str) if count_str else 5

    found_alarm = False
    for i in range(1, count + 1):
        try:
            alarm = robot.snpx.active_alarm.read(i)
            if alarm and alarm.message:
                found_alarm = True
                print(f"\n  Alarm #{i}:")
                print(f"    ID        : {alarm.id}")
                print(f"    Number    : {alarm.number}")
                print(f"    Severity  : {alarm.severity_message}")
                print(f"    Message   : {alarm.message}")
                print(f"    Cause     : {alarm.cause_message}")
                print(f"    Time      : {alarm.time}")
        except Exception as e:
            # No more alarms
            break

    if not found_alarm:
        print("\nNo active alarms.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
