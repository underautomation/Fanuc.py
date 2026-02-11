"""
SNPX - Read Digital I/O (SDI/SDO)
===================================
Read digital input or output signals via SNPX protocol.
The user selects the signal type and range.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Digital I/O Signals")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    # Available digital signal types
    signal_map = {
        "SDI": robot.snpx.sdi,
        "SDO": robot.snpx.sdo,
        "RDI": robot.snpx.rdi,
        "RDO": robot.snpx.rdo,
        "UI": robot.snpx.ui,
        "UO": robot.snpx.uo,
        "SI": robot.snpx.si,
        "SO": robot.snpx.so,
        "WI": robot.snpx.wi,
        "WO": robot.snpx.wo,
    }

    print("\nAvailable signal types:")
    print(f"  {', '.join(signal_map.keys())}")

    while True:
        sig_type = input("\nEnter signal type (e.g. SDI) [q to quit]: ").strip().upper()
        if sig_type == 'Q':
            break
        if sig_type not in signal_map:
            print(f"  Unknown type. Choose from: {', '.join(signal_map.keys())}")
            continue

        start_str = input(f"Start index for {sig_type} (default 1): ").strip()
        start = int(start_str) if start_str else 1

        count_str = input(f"Number of signals to read (default 8): ").strip()
        count = int(count_str) if count_str else 8

        # Read multiple signals at once
        values = signal_map[sig_type].read(start, count)

        print(f"\n{sig_type}[{start}] to {sig_type}[{start + count - 1}]:")
        for i, val in enumerate(values):
            state = "ON" if val else "OFF"
            print(f"  {sig_type}[{start + i}] = {state}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
