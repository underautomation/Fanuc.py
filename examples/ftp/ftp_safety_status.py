"""
FTP - Get Safety Status
========================
Read the safety status of the robot controller via FTP.
Shows E-Stop, deadman, fence, and other safety signals.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Get Safety Status")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading safety status...")
    safety = robot.ftp.get_safety_status()

    print(f"\nSafety Status:")
    print(f"  External E-Stop  : {safety.external_e_stop}")
    print(f"  SOP E-Stop       : {safety.sope_stop}")
    print(f"  TP E-Stop        : {safety.tpe_stop}")
    print(f"  Hand Broken      : {safety.hand_broken}")
    print(f"  Over Travel      : {safety.over_travel}")
    print(f"  Low Air Alarm    : {safety.low_air_alarm}")
    print(f"  Fence Open       : {safety.fence_open}")
    print(f"  Belt Broken      : {safety.belt_broken}")
    print(f"  TP Enable        : {safety.tp_enable}")
    print(f"  TP Deadman       : {safety.tp_deadman}")
    print(f"  SVOFF Detect     : {safety.svoff_detect}")
    print(f"  Non-Teacher Enb  : {safety.non_teacher_enb}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
