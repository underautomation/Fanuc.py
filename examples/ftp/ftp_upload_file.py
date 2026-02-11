"""
FTP - Upload File to Controller
=================================
Upload a local file to the robot controller via FTP.
The user specifies the local file and the remote destination.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Upload File to Controller")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    local_path = input("Enter local file path to upload: ").strip()
    if not local_path:
        print("No path provided.")
    else:
        remote_path = input("Enter remote destination path (e.g. /md/myfile.tp): ").strip()
        if not remote_path:
            print("No remote path provided.")
        else:
            print(f"\nUploading {local_path} -> {remote_path}...")
            success = robot.ftp.direct_file_handling.upload_file_to_controller(local_path, remote_path)

            if success:
                print("Upload successful!")
            else:
                print("Upload failed.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
