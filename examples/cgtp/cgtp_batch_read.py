"""
CGTP - Batch Read Variables
==============================
Read multiple variables (numeric, string, position registers) in a single
batch operation. Uses read_batch_variables().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_variables import CgtpBatchVariables

print("=" * 60)
print("  FANUC SDK - CGTP: Batch Read Variables")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    batch = CgtpBatchVariables()

    # Add numeric registers R[1] to R[5]
    for i in range(1, 6):
        batch.add_numeric_register(i)

    # Add string registers SR[1] to SR[3]
    for i in range(1, 4):
        batch.add_string_register(i)

    # Add a generic variable
    batch.add_variable("$MCR.$GENOVERRIDE")

    print(f"Reading {len(batch)} variables in a single batch...")
    result = robot.cgtp.read_batch_variables(batch)
    print(f"Controller version: {result.version}")

    print("\nResults:")
    for var in batch:
        print(f"  {var.name:<30} = {var.string_value}  (exists={var.exists})")

finally:
    robot.disconnect()
    print("\nDisconnected.")
