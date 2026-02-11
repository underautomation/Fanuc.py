"""
SNPX - Read Current World Position
====================================
Read the current Cartesian and joint position of the robot in real-time via SNPX.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Current World Position")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

try:
    group_str = input("Enter motion group number (default 1): ").strip()
    group = int(group_str) if group_str else 1

    # Read current world position
    position = robot.snpx.current_position.read_world_position(group)

    print(f"\nCurrent World Position (Group {group}):")
    print(f"  User frame: {position.user_frame}")
    print(f"  User tool : {position.user_tool}")

    cart = position.cartesian_position
    if cart:
        print(f"\n  Cartesian:")
        print(f"    X = {cart.x:.3f} mm")
        print(f"    Y = {cart.y:.3f} mm")
        print(f"    Z = {cart.z:.3f} mm")
        print(f"    W = {cart.w:.3f} deg")
        print(f"    P = {cart.p:.3f} deg")
        print(f"    R = {cart.r:.3f} deg")

    joints = position.joints_position
    if joints:
        print(f"\n  Joints:")
        print(f"    J1 = {joints.j1:.3f} deg")
        print(f"    J2 = {joints.j2:.3f} deg")
        print(f"    J3 = {joints.j3:.3f} deg")
        print(f"    J4 = {joints.j4:.3f} deg")
        print(f"    J5 = {joints.j5:.3f} deg")
        print(f"    J6 = {joints.j6:.3f} deg")

finally:
    robot.disconnect()
    print("\nDisconnected.")
