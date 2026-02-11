"""
FTP - Read Numeric Registers via File
=======================================
Read numeric registers (R[1], R[2], ...) from the robot by reading
the NUMREG variable file via FTP.

This is different from Telnet approach - FTP reads the entire file at once.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Read Numeric Registers")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading numeric registers file...")
    file = robot.ftp.known_variable_files.get_numreg_file()

    # Show how many registers exist
    print(f"\nNumeric registers count: {len(file.numreg)}")

    # Ask user which range to display
    start_str = input("\nStart register number to display (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("How many registers to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    print(f"\nRegisters R[{start}] to R[{start + count - 1}]:")
    for idx, var in enumerate(file.numreg, start=1):
        if start <= idx < start + count:
            print(f"  R[{idx}] = {var}")
    
finally:
    robot.disconnect()
    print("\nDisconnected.")
