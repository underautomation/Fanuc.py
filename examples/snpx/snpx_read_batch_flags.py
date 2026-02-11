"""
SNPX - Read Batch Flags
=========================
Read multiple flags at once using SNPX batch assignment.
Much faster than reading flags one by one.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Batch Flags")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    start_str = input("Start flag number (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("Number of flags to read (default 10): ").strip()
    count = int(count_str) if count_str else 10

    batch = robot.snpx.flags.create_batch_assignment(start, count)

    flags_values = batch.read()

    # Batch read is not available for flags through create_batch_assignment
    # Read them individually but display as a batch
    print(f"\nFlags FLG[{start}] to FLG[{start + count - 1}]:")
    for i in range(start, start + count):
        try:
            state = "ON" if flags_values[i - start] else "OFF"
            print(f"  FLG[{i}] = {state}")
        except Exception as e:
            print(f"  FLG[{i}] = Error: {e}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
