"""
FTP - Download File from Controller
=====================================
Download a file from the robot controller to the local machine via FTP.
The user specifies the remote path and local destination.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
import os

print("=" * 60)
print("  FANUC SDK - FTP: Download File from Controller")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    remote_path = input("Enter remote file path (e.g. /md:/summary.dg): ").strip()
    if not remote_path:
        print("No path provided.")
    else:
        # Default local path is current directory + filename
        filename = os.path.basename(remote_path)
        default_local = os.path.join(os.getcwd(), filename)
        local_path = input(f"Enter local save path [{default_local}]: ").strip()
        if not local_path:
            local_path = default_local

        print(f"\nDownloading {remote_path} -> {local_path}...")
        success = robot.ftp.direct_file_handling.download_file_from_controller(local_path, remote_path)

        if success:
            print(f"Download successful! File saved to: {local_path}")
        else:
            print("Download failed.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
