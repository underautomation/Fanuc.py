"""
CGTP - Pause & Abort Programs
===============================
Pause all running programs and abort a specific task on the controller.
Uses pause_all_programs() and abort_task().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Pause & Abort Programs")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    action = input("Action: (p)ause all / (a)bort task / (b)oth [p]: ").strip().lower()
    if not action:
        action = "p"

    if action in ("p", "b"):
        print("Pausing all programs...")
        robot.cgtp.pause_all_programs()
        print("All programs paused.")

    if action in ("a", "b"):
        prog = input("Program name to abort (leave empty for all): ").strip() or None
        print(f"Aborting task '{prog or 'ALL'}'...")
        robot.cgtp.abort_task(prog)
        print("Task aborted.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
