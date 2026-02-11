"""
Telnet - Get Task Information
=============================
Get information about a running task/program on the robot.
Shows task name, status, current line, program type, etc.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Telnet: Get Task Information")
print("=" * 60)

# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

try:
    while True:
        prog_name = input("Enter program/task name (e.g. MAINPROG) [q to quit]: ").strip()
        if prog_name.lower() == 'q':
            break
        if not prog_name:
            continue

        result = robot.telnet.get_task_information(prog_name)

        if result.succeed:
            print(f"\nTask Information for '{prog_name}':")
            print(f"  Task name      : {result.task_name}")
            print(f"  Task number    : {result.task_number}")
            print(f"  Status         : {result.task_status_str}")
            print(f"  Routine name   : {result.routine_name}")
            print(f"  Current line   : {result.current_line}")
            print(f"  Program type   : {result.program_type}")
            print(f"  Hold conditions: {result.hold_conditions}")
            print(f"  Invisible task : {result.invisible_task}")
            print(f"  System task    : {result.system_task}")
        else:
            print(f"  Error: {result.error_text}")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
