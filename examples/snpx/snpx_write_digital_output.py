"""
SNPX - Write Digital Output
==============================
Write digital output signals (SDO, RDO, etc.) via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Write Digital Output")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    # Writable output signal types
    signal_map = {
        "SDO": robot.snpx.sdo,
        "RDO": robot.snpx.rdo,
        "UO": robot.snpx.uo,
        "SO": robot.snpx.so,
        "WO": robot.snpx.wo,
    }

    print("\nWritable output signal types:")
    print(f"  {', '.join(signal_map.keys())}")

    while True:
        sig_type = input("\nEnter signal type (e.g. SDO) [q to quit]: ").strip().upper()
        if sig_type == 'Q':
            break
        if sig_type not in signal_map:
            print(f"  Unknown type. Choose from: {', '.join(signal_map.keys())}")
            continue

        index_str = input(f"Signal index: ").strip()
        try:
            index = int(index_str)
        except ValueError:
            print("  Invalid number.")
            continue

        value_str = input(f"Value (1=ON, 0=OFF): ").strip()
        try:
            value = bool(int(value_str))
        except ValueError:
            print("  Invalid value.")
            continue

        # Write single signal (write takes a start index and a list of values)
        signal_map[sig_type].write(index, [value])
        print(f"  {sig_type}[{index}] set to {'ON' if value else 'OFF'}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
