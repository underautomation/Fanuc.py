"""
SNPX - Read Multiple Numeric Registers (Batch)
================================================
Read a batch of numeric registers at once using SNPX assignment.
Much faster than reading one by one for multiple registers.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Multiple Numeric Registers")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    start_str = input("Start register number (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("Number of registers to read (default 10): ").strip()
    count = int(count_str) if count_str else 10

    # Create a batch assignment for efficient reading
    batch = robot.snpx.numeric_registers.create_batch_assignment(start, count)
    values = batch.read()

    print(f"\nRegisters R[{start}] to R[{start + count - 1}]:")
    for i, val in enumerate(values):
        print(f"  R[{start + i}] = {val}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
