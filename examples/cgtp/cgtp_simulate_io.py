"""
CGTP - Simulate & Unsimulate I/O
==================================
Simulate, unsimulate and check simulation status of I/O ports.
Uses simulate_io(), unsimulate_io() and get_io_simulation_status().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.cgtp_io_port_type import CgtpIoPortType

print("=" * 60)
print("  FANUC SDK - CGTP: Simulate & Unsimulate I/O")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

available = ", ".join(pt.name for pt in CgtpIoPortType)

try:
    type_str = input(f"\nI/O type ({available}): ").strip()
    port_type = CgtpIoPortType[type_str]

    idx = int(input("Port index: ").strip())

    # Check current simulation status
    simulated = robot.cgtp.get_io_simulation_status(port_type, idx)
    print(f"\n  {port_type.name}[{idx}] simulated: {simulated}")

    action = input("Action: (s)imulate / (u)nsimulate [s]: ").strip().lower()
    if not action:
        action = "s"

    if action == "s":
        robot.cgtp.simulate_io(port_type, idx)
        print(f"  {port_type.name}[{idx}] is now simulated.")
    else:
        robot.cgtp.unsimulate_io(port_type, idx)
        print(f"  {port_type.name}[{idx}] simulation removed.")

    # Verify
    simulated = robot.cgtp.get_io_simulation_status(port_type, idx)
    print(f"  {port_type.name}[{idx}] simulated: {simulated}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
