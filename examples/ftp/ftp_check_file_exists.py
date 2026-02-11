"""
FTP - Check File Exists
========================
Check if a specific file or directory exists on the robot controller via FTP.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.ftp.ftp_file_system_object_type import FtpFileSystemObjectType

print("=" * 60)
print("  FANUC SDK - FTP: Check File Exists")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    while True:
        path = input("Enter file or directory path to check (e.g. /md:/summary.dg) [q to quit]: ").strip()
        if path.lower() == 'q':
            break
        if not path:
            continue

        file_exists = robot.ftp.direct_file_handling.file_exists(path)
        dir_exists = robot.ftp.direct_file_handling.directory_exists(path)

        if file_exists:
            info = robot.ftp.direct_file_handling.get_object_info(path)
            type_names = {int(FtpFileSystemObjectType.File): "File", int(FtpFileSystemObjectType.Directory): "Directory", int(FtpFileSystemObjectType.Link): "Link"}
            type_name = type_names.get(int(info.type), str(info.type))
            print(f"  File exists: {info.name} (Type : {type_name})")
        elif dir_exists:
            print(f"  Directory exists: {path}")
        else:
            print(f"  Not found: {path}")
        print()

finally:
    robot.disconnect()
    print("Disconnected.")
