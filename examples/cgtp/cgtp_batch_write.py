"""
CGTP - Batch Write Variables
===============================
Write multiple variables (numeric and string registers) to the controller
in a single batch operation. Uses write_batch_variables().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_variables import CgtpBatchVariables

print("=" * 60)
print("  FANUC SDK - CGTP: Batch Write Variables")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    batch = CgtpBatchVariables()

    # Add numeric registers with values
    batch.add_numeric_register_as_integer(1, "Batch int", 42)
    batch.add_numeric_register_as_real(2, "Batch real", 3.14)

    # Add string register with value
    batch.add_string_register_with_value(1, "Batch str", "Hello CGTP")

    # Add a system variable
    batch.add_variable("$MCR.$GENOVERRIDE").integer_value = 50

    print(f"\nThe following {len(batch)} variables will be written:")
    for var in batch:
        print(f"  {var.name:<30} = {var.string_value}")

    confirm = input("\nProceed with write? (Y/n) [Y]: ").strip().lower()
    if confirm and confirm != "y":
        print("Write cancelled.")
    else:
        print(f"\nWriting {len(batch)} variables in a single batch...")
        result = robot.cgtp.write_batch_variables(batch)
        print("Batch write completed.")

    # Verify by reading back
    # We create a new batch for reading to avoid any state issues with the write batch, but you could reuse the same batch if desired.
    read_batch = CgtpBatchVariables()
    read_batch.add_numeric_register(1)
    read_batch.add_numeric_register(2)
    read_batch.add_string_register(1)

    robot.cgtp.read_batch_variables(read_batch)
    print("\nVerification:")
    for var in read_batch:
        print(f"  {var.name:<30} = {var.string_value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
