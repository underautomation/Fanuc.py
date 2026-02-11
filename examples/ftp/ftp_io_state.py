"""
FTP - Get I/O State
====================
Read all digital I/O states (DIN, DOUT, RI, RO, UI, UO, SI, SO, FLG) via FTP.
Displays port name, index, value and configured name.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.digital_ports import DigitalPorts
from collections import defaultdict

# Build a reverse mapping: int value -> port name
PORT_NAMES = {v: k for k, v in vars(DigitalPorts).items() if isinstance(v, int)}

print("=" * 60)
print("  FANUC SDK - FTP: Get I/O State")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading I/O state (this may take a moment)...")
    io_state = robot.ftp.get_io_state()

    # Group I/Os by port type
    groups = defaultdict(list)
    for io in io_state.states:
        groups[io.port].append(io)

    print(f"\nTotal I/O signals: {len(io_state.states)}")

    # Display each port type in a multi-column layout
    NUM_COLUMNS = 4
    for port_value, signals in groups.items():
        port_name = PORT_NAMES.get(port_value, str(port_value))
        print(f"\n{'=' * 60}")
        print(f"  {port_name} ({len(signals)} signals)")
        print(f"{'=' * 60}")

        # Format each signal as a compact string
        entries = []
        for io in signals:
            value_str = "ON " if io.value else "OFF"
            label = f" {io.id:>4} {value_str}"
            if io.name:
                label += f" {io.name}"
            entries.append(label)

        # Find the max width for even columns
        col_width = max((len(e) for e in entries), default=10) + 2

        # Print in columns
        for i in range(0, len(entries), NUM_COLUMNS):
            row = entries[i:i + NUM_COLUMNS]
            print("".join(e.ljust(col_width) for e in row))

finally:
    robot.disconnect()
    print("\nDisconnected.")
