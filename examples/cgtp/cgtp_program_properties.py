"""
CGTP - Get & Set Program Properties
=====================================
Read and write program properties: comment, owner, stack size,
ignore pause, write protect, and sub-type.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Program Properties")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    prog = input("Program name (e.g. MAIN): ").strip()
    if not prog:
        prog = "MAIN"

    # Read all properties
    print(f"\nProperties of '{prog}':")
    print(f"  Comment       : {robot.cgtp.get_program_comment(prog)}")
    print(f"  Owner         : {robot.cgtp.get_program_owner(prog)}")
    print(f"  Stack size    : {robot.cgtp.get_program_stack_size(prog)}")
    print(f"  Ignore pause  : {robot.cgtp.get_program_ignore_pause(prog)}")
    print(f"  Write protect : {robot.cgtp.get_program_write_protect(prog)}")
    print(f"  Sub-type      : {robot.cgtp.get_program_sub_type(prog)}")

    # Optionally set comment
    new_comment = input("\nNew comment (leave empty to skip): ").strip()
    if new_comment:
        robot.cgtp.set_program_comment(prog, new_comment)
        print(f"  Comment updated to: {robot.cgtp.get_program_comment(prog)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
