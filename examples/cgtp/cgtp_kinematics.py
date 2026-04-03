"""
CGTP - Forward & Inverse Kinematics
=====================================
Compute forward kinematics (joints to Cartesian) and inverse kinematics
(Cartesian to joints) on the controller via CGTP.
Uses forward_kinematics() and invert_kinematics().
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - CGTP: Forward & Inverse Kinematics")
print("=" * 60)

robot = connect_robot(enable_cgtp=True)

try:
    group_str = input("Motion group number (default 1): ").strip()
    group = int(group_str) if group_str else 1

    # Read current positions
    joints = robot.cgtp.read_joint_position(group)
    cart = robot.cgtp.read_cartesian_position(group)

    print(f"\nCurrent joint position (Group {group}):")
    print(f"  J1={joints.j1:.3f}  J2={joints.j2:.3f}  J3={joints.j3:.3f}")
    print(f"  J4={joints.j4:.3f}  J5={joints.j5:.3f}  J6={joints.j6:.3f}")

    # Forward kinematics: joints -> cartesian
    print("\nForward kinematics (current joints -> Cartesian):")
    fk_result = robot.cgtp.forward_kinematics(group, joints)
    print(f"  X={fk_result.x:.3f}  Y={fk_result.y:.3f}  Z={fk_result.z:.3f}")
    print(f"  W={fk_result.w:.3f}  P={fk_result.p:.3f}  R={fk_result.r:.3f}")

    # Inverse kinematics: cartesian -> joints
    print("\nInverse kinematics (current Cartesian -> joints):")
    ik_result = robot.cgtp.invert_kinematics(group, cart)
    print(f"  J1={ik_result.j1:.3f}  J2={ik_result.j2:.3f}  J3={ik_result.j3:.3f}")
    print(f"  J4={ik_result.j4:.3f}  J5={ik_result.j5:.3f}  J6={ik_result.j6:.3f}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
