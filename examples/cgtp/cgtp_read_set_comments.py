"""
CGTP - Read & Set Comments
============================
Read all comments for a given type (registers, I/O, etc.) and set a comment.
Uses get_comments() and set_comment().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.cgtp.cgtp_comment_type import CgtpCommentType

print("=" * 60)
print("  FANUC SDK - CGTP: Read & Set Comments")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    available = ", ".join(ct.name for ct in CgtpCommentType)
    type_str = input(f"\nComment type ({available}): ").strip()
    comment_type = CgtpCommentType[type_str]

    print(f"\nReading {comment_type.name} comments...")
    comments = robot.cgtp.get_comments(comment_type)
    print(f"Total comments: {len(comments)}")

    count_str = input("How many to display (default 10): ").strip()
    count = int(count_str) if count_str else 10

    for i in range(min(count, len(comments))):
        c = comments[i]
        if c:
            print(f"  [{i + 1:>3}] {c}")

    # Set a comment
    idx_str = input("\nSet comment at index (leave empty to skip): ").strip()
    if idx_str:
        idx = int(idx_str)
        new_comment = input("New comment: ").strip()
        robot.cgtp.set_comment(comment_type, idx, new_comment)
        print(f"  Comment [{idx}] updated.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
