"""
FTP - Read String Registers via File
======================================
Read string registers (SR[1], SR[2], ...) from the robot by reading
the STRREG variable file via FTP.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Read String Registers")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading string registers file...")
    file = robot.ftp.known_variable_files.get_strreg_file()

    print(f"\nString registers count: {len(file.strreg)}")

    # Ask user which range to display
    start_str = input("\nStart SR number (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("How many to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    print(f"\nString registers SR[{start}] to SR[{start + count - 1}]:")
    for idx, var in enumerate(file.strreg, start=1):
        if start <= idx < start + count:
            print(f"  SR[{idx}] = \"{var}\"")

finally:
    robot.disconnect()
    print("\nDisconnected.")
