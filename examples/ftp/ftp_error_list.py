"""
FTP - Get Error List
=====================
Retrieve the complete error/alarm history from the robot controller via FTP.
Shows error codes, messages, timestamps, and whether they are still active.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Get Error List")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading error list...")
    error_list = robot.ftp.get_all_errors_list()

    # Show all errors
    print(f"\nTotal errors in history: {len(error_list.items)}")
    print(f"{'#':<6} {'Code':<14} {'Time':<22} {'Message'}")
    print("-" * 80)
    for err in error_list.items:
        code = err.error_code if err.error_code is not None or not err.is_reset else "(Reset)"
        print(f"  {err.id:<4} {str(code):<14} {str(err.occurring_time):<22} {err.message}")

    # Show only active alarms
    active = error_list.filter_active_alarms()
    print(f"\nActive alarms: {len(active)}")
    for alarm in active:
        print(f"  [{alarm.error_code}] {alarm.message}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
