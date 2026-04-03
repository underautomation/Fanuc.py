"""
CGTP - Read I/O Comments
==========================
Read input and output comments for an I/O type (Robot, Digital, Group, Analog).
Uses get_io_comments().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.cgtp_comment_io_type import CgtpCommentIoType

print("=" * 60)
print("  FANUC SDK - CGTP: Read I/O Comments")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    available = ", ".join(ct.name for ct in CgtpCommentIoType)
    type_str = input(f"\nI/O comment type ({available}): ").strip()
    io_type = CgtpCommentIoType[type_str]

    print(f"\nReading {io_type.name} comments...")
    io_comments = robot.cgtp.get_io_comments(io_type)

    count_str = input("How many to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    print(f"\nInput comments:")
    for i, c in enumerate(list(io_comments.inputs)[:count], 1):
        if c:
            print(f"  [{i:>3}] {c}")

    print(f"\nOutput comments:")
    for i, c in enumerate(list(io_comments.outputs)[:count], 1):
        if c:
            print(f"  [{i:>3}] {c}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
