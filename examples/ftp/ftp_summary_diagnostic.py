"""
FTP - Get Summary Diagnostic
==============================
Retrieve a complete summary diagnostic from the robot via FTP.
Includes robot position, safety status, I/O states, features, and programs.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Get Summary Diagnostic")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading summary diagnostic...")
    diag = robot.ftp.get_summary_diagnostic()

    print(f"\nDiagnostic name: {diag.name}")

    # ---- Current Position ----
    print("\n--- Current Position ---")
    for gp in diag.current_position.groups_position:
        jp = gp.joints_position
        print(f"  Group {gp.id} joints: J1={jp.j1:.2f}  J2={jp.j2:.2f}  J3={jp.j3:.2f}  J4={jp.j4:.2f}  J5={jp.j5:.2f}  J6={jp.j6:.2f}")

        for wp in gp.world_positions:
            print(f"    World (tool {wp.tool}): X={wp.x:.2f}  Y={wp.y:.2f}  Z={wp.z:.2f}  W={wp.w:.2f}  P={wp.p:.2f}  R={wp.r:.2f}")

    # ---- Safety Status ----
    print("\n--- Safety Status ---")
    safety = diag.safety
    print(f"  External E-Stop : {safety.external_e_stop}")
    print(f"  TP E-Stop       : {safety.tpe_stop}")
    print(f"  TP Enable       : {safety.tp_enable}")
    print(f"  TP Deadman      : {safety.tp_deadman}")
    print(f"  Fence Open      : {safety.fence_open}")
    print(f"  Over Travel     : {safety.over_travel}")
    print(f"  SVOFF Detect    : {safety.svoff_detect}")

    # ---- Features ----
    print("\n--- Features ---")
    print(f"  Has Telnet      : {diag.features.has_telnet}")
    print(f"  Has SNPX        : {diag.features.has_snpx}")
    print(f"  Has ASCII Upload: {diag.features.has_ascii_upload}")
    print(f"  Features count  : {len(diag.features.features_list)}")

    # ---- Program States ----
    print("\n--- Program States ---")
    for task in diag.program_states.task_states:
        print(f"  Task #{task.number}: {task.name} - {task.status}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
