"""
FTP - Read System Variables
=============================
Read system variables from the robot via FTP using the SYSTEM variable file.
Shows a selection of commonly used system variables.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Read System Variables")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading system variable file (this may take a moment)...")
    system = robot.ftp.known_variable_files.get_system_file()

    # Display commonly used system variables
    print(f"\nSystem Variables:")
    print(f"  Robot name     : {system.robot_name}")
    print(f"  Hostname       : {system.hostname}")
    print(f"  Language       : {system.language}")
    print(f"  Timer count    : {system.timer_num}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
