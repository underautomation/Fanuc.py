"""
FTP - Get Program States
=========================
Read the state of all running tasks/programs via FTP.
Shows task number, name, status, and call history.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Get Program States")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading program states...")
    prog_states = robot.ftp.get_program_states()

    if not prog_states.task_states:
        print("\nNo tasks found.")
    else:
        print(f"\n{'#':<6} {'Name':<20} {'Status':<12}")
        print("-" * 40)
        for task in prog_states.task_states:
            print(f"  {task.number:<4} {task.name:<20} {task.status}")
            # Show call history if available
            if task.history:
                for h in task.history:
                    print(f"         -> {h.program_name} / {h.routine_name} (line {h.line_number}, {h.program_type})")
            print("")

finally:
    robot.disconnect()
    print("\nDisconnected.")
