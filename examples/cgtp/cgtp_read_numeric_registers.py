"""
CGTP - Read Numeric Registers
===============================
Read all numeric registers (R[]) with their comments and values.
Uses read_numeric_registers_with_comment() and read_numeric_register_with_comment().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Read Numeric Registers")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    print("Reading all numeric registers...")
    registers = robot.cgtp.read_numeric_registers_with_comment()
    print(f"Total registers: {len(registers)}")

    start_str = input("\nStart index to display (default 1): ").strip()
    start = int(start_str) if start_str else 1

    count_str = input("How many to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    print(f"\nRegisters R[{start}] to R[{start + count - 1}]:")
    for i in range(start - 1, min(start - 1 + count, len(registers))):
        reg = registers[i]
        print(f"  R[{i + 1:>3}] = {reg}")

    # Read a single register
    idx_str = input("\nRead single register index (leave empty to skip): ").strip()
    if idx_str:
        idx = int(idx_str)
        reg = robot.cgtp.read_numeric_register_with_comment(idx)
        print(f"  R[{idx}] = {reg}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
