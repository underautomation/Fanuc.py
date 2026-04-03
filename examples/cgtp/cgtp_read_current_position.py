"""
CGTP - Read Current Position
==============================
Read the current Cartesian and joint position of the robot.
Uses read_cartesian_position() and read_joint_position().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Read Current Position")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    group_str = input("Motion group number (default 1): ").strip()
    group = int(group_str) if group_str else 1

    # Cartesian position
    cart = robot.cgtp.read_cartesian_position(group)
    print(f"\nCartesian Position (Group {group}):")
    print(f"  X = {cart.x:.3f} mm")
    print(f"  Y = {cart.y:.3f} mm")
    print(f"  Z = {cart.z:.3f} mm")
    print(f"  W = {cart.w:.3f} deg")
    print(f"  P = {cart.p:.3f} deg")
    print(f"  R = {cart.r:.3f} deg")

    # Joint position
    joints = robot.cgtp.read_joint_position(group)
    print(f"\nJoint Position (Group {group}):")
    print(f"  J1 = {joints.j1:.3f} deg")
    print(f"  J2 = {joints.j2:.3f} deg")
    print(f"  J3 = {joints.j3:.3f} deg")
    print(f"  J4 = {joints.j4:.3f} deg")
    print(f"  J5 = {joints.j5:.3f} deg")
    print(f"  J6 = {joints.j6:.3f} deg")

finally:
    robot.disconnect()
    print("\nDisconnected.")
