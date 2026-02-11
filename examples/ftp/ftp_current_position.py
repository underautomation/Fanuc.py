"""
FTP - Get Current Position
===========================
Read the current robot position (joints + Cartesian) via FTP.
Shows all motion groups with joint angles and world coordinates.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - FTP: Get Current Position")
print("=" * 60)

# Connect with FTP enabled
robot = connect_robot(enable_ftp=True)

try:
    print("Reading current position...")
    position = robot.ftp.get_current_position()

    for gp in position.groups_position:
        jp = gp.joints_position
        print(f"\nGroup {gp.id} - Joint Position:")
        print(f"  J1 = {jp.j1:.3f} deg")
        print(f"  J2 = {jp.j2:.3f} deg")
        print(f"  J3 = {jp.j3:.3f} deg")
        print(f"  J4 = {jp.j4:.3f} deg")
        print(f"  J5 = {jp.j5:.3f} deg")
        print(f"  J6 = {jp.j6:.3f} deg")

        for wp in gp.world_positions:
            print(f"\n  World Position (Tool {wp.tool}):")
            print(f"    X = {wp.x:.3f} mm")
            print(f"    Y = {wp.y:.3f} mm")
            print(f"    Z = {wp.z:.3f} mm")
            print(f"    W = {wp.w:.3f} deg")
            print(f"    P = {wp.p:.3f} deg")
            print(f"    R = {wp.r:.3f} deg")
            print(f"    Conf = {wp.configuration}")

        for uf in gp.user_frame_positions:
            print(f"\n  User Frame {uf.frame} Position:")
            print(f"    X = {uf.x:.3f} mm")
            print(f"    Y = {uf.y:.3f} mm")
            print(f"    Z = {uf.z:.3f} mm")
            print(f"    W = {uf.w:.3f} deg")
            print(f"    P = {uf.p:.3f} deg")
            print(f"    R = {uf.r:.3f} deg")

finally:
    robot.disconnect()
    print("\nDisconnected.")
