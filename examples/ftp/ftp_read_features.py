"""
FTP - Read Robot Features
==========================
Read the installed features/options on the robot controller via FTP.
Shows the list of software options with their order numbers.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Read Robot Features")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading diagnostic to get features...")
    diag = robot.ftp.get_summary_diagnostic()

    features = diag.features

    print(f"\nInstalled features ({len(features.features_list)}):")
    print(f"  {'Order No':<15} {'Name'}")
    print("  " + "-" * 50)
    for feat in features.features_list:
        print(f"  {feat.order_no:<15} {feat.name}")

    print(f"\nProtocol support:")
    print(f"  Has Telnet       : {features.has_telnet}")
    print(f"  Has SNPX         : {features.has_snpx}")
    print(f"  Has ASCII Upload : {features.has_ascii_upload}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
