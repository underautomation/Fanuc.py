"""
SNPX - Read Numeric I/O (GI/GO/AI/AO)
========================================
Read numeric (group/analog) I/O values via SNPX protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Numeric I/O")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    signal_map = {
        "GI": robot.snpx.gi,
        "GO": robot.snpx.go,
        "AI": robot.snpx.ai,
        "AO": robot.snpx.ao,
    }

    print("\nAvailable numeric I/O types:")
    print(f"  {', '.join(signal_map.keys())}")

    while True:
        sig_type = input("\nEnter I/O type (e.g. GI) [q to quit]: ").strip().upper()
        if sig_type == 'Q':
            break
        if sig_type not in signal_map:
            print(f"  Unknown type. Choose from: {', '.join(signal_map.keys())}")
            continue

        start_str = input(f"Start index (default 1): ").strip()
        start = int(start_str) if start_str else 1

        count_str = input(f"Number to read (default 5): ").strip()
        count = int(count_str) if count_str else 5

        values = signal_map[sig_type].read(start, count)

        print(f"\n{sig_type}[{start}] to {sig_type}[{start + count - 1}]:")
        for i, val in enumerate(values):
            print(f"  {sig_type}[{start + i}] = {val}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
