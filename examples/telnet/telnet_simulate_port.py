"""
Telnet - Simulate / Unsimulate Port
====================================
Simulate a digital I/O port so the controller treats it as a fixed value,
then unsimulate it to restore normal operation.

Useful for testing without real I/O devices connected.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.telnet.kcl_ports import KCLPorts

print("=" * 60)
print("  FANUC SDK - Telnet: Simulate / Unsimulate Port")
print("=" * 60)


# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

port_map = {
    "DIN": KCLPorts.DIN,
    "DOUT": KCLPorts.DOUT,
    "RDO": KCLPorts.RDO,
}

print("\nAvailable port types for simulation:")
for name in port_map:
    print(f"  - {name}")

try:
    while True:
        print("\nOptions:")
        print("  1 - Simulate a port")
        print("  2 - Unsimulate a port")
        print("  3 - Unsimulate ALL ports")
        print("  q - Quit")
        choice = input("Choice: ").strip()

        if choice == 'q':
            break
        elif choice == '1':
            port_name = input("Port type (DIN, DOUT, RDO): ").strip().upper()
            if port_name not in port_map:
                print("  Unknown port type.")
                continue
            index = int(input(f"Port index: "))
            value = int(input("Simulated value (0 or 1): "))

            result = robot.telnet.simulate(port_map[port_name], index, value)
            if result.succeed:
                print(f"  {port_name}[{index}] simulated to {value}")
            else:
                print(f"  Error: {result.error_text}")

        elif choice == '2':
            port_name = input("Port type (DIN, DOUT, RDO): ").strip().upper()
            if port_name not in port_map:
                print("  Unknown port type.")
                continue
            index = int(input(f"Port index: "))

            result = robot.telnet.unsimulate(port_map[port_name], index)
            if result.succeed:
                print(f"  {port_name}[{index}] unsimulated")
            else:
                print(f"  Error: {result.error_text}")

        elif choice == '3':
            result = robot.telnet.unsimulate_all()
            if result.succeed:
                print("  All ports unsimulated")
            else:
                print(f"  Error: {result.error_text}")
finally:
    robot.disconnect()
    print("Disconnected.")
