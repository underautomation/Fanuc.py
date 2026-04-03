"""
CGTP - Read & Write I/O
=========================
Read and write I/O ports (DI, DO, RI, RO, GI, GO, AI, AO, Flag).
Uses read_io() and write_io().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.cgtp_io_port_type import CgtpIoPortType

print("=" * 60)
print("  FANUC SDK - CGTP: Read & Write I/O")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

available = ", ".join(pt.name for pt in CgtpIoPortType)

try:
    while True:
        type_str = input(f"\nI/O type ({available}) [q to quit]: ").strip()
        if type_str.lower() == "q":
            break

        try:
            port_type = CgtpIoPortType[type_str]
        except KeyError:
            print(f"  Unknown type '{type_str}'")
            continue

        idx = int(input("Port index: ").strip())

        # Read
        value = robot.cgtp.read_io(port_type, idx)
        print(f"  {port_type.name}[{idx}] = {value}")

        # Optionally write
        new_val = input(f"  New value for {port_type.name}[{idx}] (leave empty to skip): ").strip()
        if new_val:
            robot.cgtp.write_io(port_type, idx, int(new_val))
            value = robot.cgtp.read_io(port_type, idx)
            print(f"  {port_type.name}[{idx}] updated to {value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
