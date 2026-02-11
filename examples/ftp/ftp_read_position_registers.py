"""
FTP - Read Position Registers via File
========================================
Read position registers (PR[1], PR[2], ...) from the robot by reading
the POSREG variable file via FTP.

Shows both Cartesian and joint representation of each position.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Read Position Registers")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading position registers file...")
    file = robot.ftp.known_variable_files.get_posreg_file()

    print(f"\nPosition registers count: {len(file.posreg)}")

    # Ask user which range to display
    start_str = input("\nStart PR number (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("How many to display (default 5): ").strip()
    count = int(count_str) if count_str else 5

    print(f"\nPosition registers PR[{start}] to PR[{start + count - 1}]:")
    for idx, var in enumerate(file.posreg, start=1):
        if start <= idx < start + count:
            print(f"\n  PR[{idx}]: {var}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
