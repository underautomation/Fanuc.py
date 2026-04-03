"""
CGTP - Read User Alarms
=========================
Read all user alarm definitions with their comments and severity.
Uses read_user_alarms() and set_user_alarm_severity().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Read User Alarms")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    print("Reading user alarms...")
    alarms = robot.cgtp.read_user_alarms()
    print(f"Total user alarms: {len(alarms)}")

    count_str = input("\nHow many to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    for i, alarm in enumerate(alarms[:count], 1):
        print(f"  [{i:>3}] {alarm}")

    # Optionally change severity
    idx_str = input("\nSet severity at index (leave empty to skip): ").strip()
    if idx_str:
        idx = int(idx_str)
        sev = int(input("New severity: ").strip())
        robot.cgtp.set_user_alarm_severity(idx, sev)
        print(f"  User alarm [{idx}] severity updated to {sev}.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
