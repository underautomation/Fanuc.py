"""
Telnet - Program Control (Run, Pause, Resume, Task Info, Abort)
================================================================
Demonstrates full program lifecycle control via Telnet KCL:
  1. Run a program
  2. Pause the running program
  3. Resume (continue) the paused program
  4. Get task information while running
  5. Abort the program

All operations use the Telnet interface only.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Telnet: Program Control")
print("=" * 60)

# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

try:
    # ---- Check remote master configuration ----
    print("\nChecking remote master configuration...")
    rmt_master = robot.telnet.get_variable("$RMT_MASTER")
    remote_type = robot.telnet.get_variable("$REMOTE_CFG.$REMOTE_TYPE")

    needs_update = False
    if rmt_master.succeed and rmt_master.raw_value.strip() != "1":
        print(f"  $RMT_MASTER = {rmt_master.raw_value.strip()} (expected 1)")
        needs_update = True
    if remote_type.succeed and remote_type.raw_value.strip() != "1":
        print(f"  $REMOTE_CFG.$REMOTE_TYPE = {remote_type.raw_value.strip()} (expected 1)")
        needs_update = True

    if needs_update:
        print("\n  To start programs via Telnet KCL, the controller must be configured")
        print("  with KCL as the master device:")
        print("    $RMT_MASTER = 1")
        print("    $REMOTE_CFG.$REMOTE_TYPE = 1")
        answer = input("\n  Set these variables to 1 now? (y/n): ").strip().lower()
        if answer == 'y':
            r1 = robot.telnet.set_variable("$RMT_MASTER", 1)
            r2 = robot.telnet.set_variable("$REMOTE_CFG.$REMOTE_TYPE", 1)
            if r1.succeed and r2.succeed:
                print("  Variables updated successfully.")
            else:
                if not r1.succeed:
                    print(f"  Error setting $RMT_MASTER: {r1.error_text}")
                if not r2.succeed:
                    print(f"  Error setting $REMOTE_CFG.$REMOTE_TYPE: {r2.error_text}")
                print("  You may need to set them manually on the teach pendant.")
        else:
            print("  Skipped. Program start may fail without these settings.")
    else:
        print("  Remote master configuration OK.")

    prog_name = input("\nEnter program name to control (e.g. MAINPROG): ").strip()
    if not prog_name:
        print("No program name provided. Exiting.")
        sys.exit(0)

    # ---- 1. Run the program ----
    while True:
        print(f"\n[1/5] Running program '{prog_name}'...")
        result = robot.telnet.run(prog_name)
        if result.succeed:
            print(f"  Program started successfully.")
            break
        else:
            print(f"  Error: {result.error_text}")
            new_name = input(f"  Enter a new program name [{prog_name}] or 'q' to quit: ").strip()
            if new_name.lower() == 'q':
                print("Exiting.")
                sys.exit(0)
            if new_name:
                prog_name = new_name

    input("\nPress Enter to pause the program...")

    # ---- 2. Pause the program ----
    print(f"\n[2/5] Pausing program '{prog_name}'...")
    result = robot.telnet.pause(prog_name)
    if result.succeed:
        print(f"  Program paused successfully.")
    else:
        print(f"  Error: {result.error_text}")

    # ---- 3. Get task information ----
    print(f"\n[3/5] Getting task information for '{prog_name}'...")
    info = robot.telnet.get_task_information(prog_name)
    if info.succeed:
        print(f"  Task name      : {info.task_name}")
        print(f"  Task number    : {info.task_number}")
        print(f"  Status         : {info.task_status_str}")
        print(f"  Routine name   : {info.routine_name}")
        print(f"  Current line   : {info.current_line}")
        print(f"  Program type   : {info.program_type}")
        print(f"  Hold conditions: {info.hold_conditions}")
    else:
        print(f"  Error: {info.error_text}")

    input("\nPress Enter to resume the program...")

    # ---- 4. Resume (continue) the program ----
    print(f"\n[4/5] Resuming program '{prog_name}'...")
    result = robot.telnet.continue_(prog_name)
    if result.succeed:
        print(f"  Program resumed successfully.")
    else:
        print(f"  Error: {result.error_text}")

    input("\nPress Enter to abort the program...")

    # ---- 5. Abort the program ----
    print(f"\n[5/5] Aborting program '{prog_name}'...")
    result = robot.telnet.abort(prog_name)
    if result.succeed:
        print(f"  Program aborted successfully.")
    else:
        print(f"  Error: {result.error_text}")

    print("\nProgram control demo complete.")

finally:
    robot.disconnect()
    print("Disconnected.")
