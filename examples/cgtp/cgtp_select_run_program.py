"""
CGTP - Select & Run Program
=============================
Select a TP program on the controller and run it from a given line.
Uses select_program() and run_program().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Select & Run Program")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    prog = input("Program name to select (e.g. MAIN): ").strip()
    if not prog:
        prog = "MAIN"

    line_str = input("Line number (default 1): ").strip()
    line = int(line_str) if line_str else 1

    print(f"\nSelecting program '{prog}' at line {line}...")
    robot.cgtp.select_program(prog, line)
    print("Program selected.")

    run = input("\nRun the program? (y/n) [n]: ").strip().lower()
    if run == "y":
        robot.cgtp.run_program(prog, line)
        print("Program started.")
    else:
        print("Skipped.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
