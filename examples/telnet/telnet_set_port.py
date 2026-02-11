"""
Telnet - Set Digital Output Port
=================================
Set a digital output port (DOUT, RDO, etc.) via Telnet KCL.
The user chooses the port type, index, and value (ON=1, OFF=0).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.telnet.kcl_ports import KCLPorts

print("=" * 60)
print("  FANUC SDK - Telnet: Set Digital Output Port")
print("=" * 60)

# Show available port types
port_map = {
    "DOUT": KCLPorts.DOUT,
    "RDO": KCLPorts.RDO,
    "OPOUT": KCLPorts.OPOUT,
    "TPOUT": KCLPorts.TPOUT,
    "GOUT": KCLPorts.GOUT,
}


# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

print("\nAvailable output port types:")
for name in port_map:
    print(f"  - {name}")
    
try:
    while True:
        port_name = input("\nEnter port type (e.g. DOUT) [q to quit]: ").strip().upper()
        if port_name == 'Q':
            break
        if port_name not in port_map:
            print(f"  Unknown port type. Choose from: {', '.join(port_map.keys())}")
            continue

        index_str = input(f"Enter {port_name} index (e.g. 1): ").strip()
        try:
            index = int(index_str)
        except ValueError:
            print("  Invalid number.")
            continue

        value_str = input(f"Enter value (1=ON, 0=OFF): ").strip()
        try:
            value = int(value_str)
            if value not in (0, 1):
                raise ValueError
        except ValueError:
            print("  Invalid value. Enter 0 or 1.")
            continue

        # Set the port
        result = robot.telnet.set_port(port_map[port_name], index, value)

        if result.succeed:
            print(f"  {port_name}[{index}]: {result.former_value} -> {result.new_value}")
        else:
            print(f"  Error: {result.error_text}")
finally:
    robot.disconnect()
    print("Disconnected.")
