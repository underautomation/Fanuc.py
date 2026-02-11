"""
SNPX - Write Position Register
================================
Write a position register (PR[i]) via SNPX protocol.
Supports both Cartesian and Joint representations.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition

print("=" * 60)
print("  FANUC SDK - SNPX: Write Position Register")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

def input_float(prompt, current_value):
    """Prompt for a float value, showing current value. Keep current if empty."""
    if current_value is not None:
        raw = input(f"    {prompt} ({current_value:.3f}): ").strip()
    else:
        raw = input(f"    {prompt}: ").strip()
    if raw == "":
        return current_value if current_value is not None else 0.0
    return float(raw)

try:
    while True:
        pr_str = input("Enter position register number (e.g. 1 for PR[1]) [q to quit]: ").strip()
        if pr_str.lower() == 'q':
            break

        try:
            pr_num = int(pr_str)
        except ValueError:
            print("  Invalid number.")
            continue

        # Read current position register
        pos = robot.snpx.position_registers.read(pr_num)
        cart = pos.cartesian_position
        joints = pos.joints_position

        print(f"\n  PR[{pr_num}] current value:")

        if cart._instance:
            print(f"    Cartesian:")
            print(f"      X = {cart.x:.3f} mm")
            print(f"      Y = {cart.y:.3f} mm")
            print(f"      Z = {cart.z:.3f} mm")
            print(f"      W = {cart.w:.3f} deg")
            print(f"      P = {cart.p:.3f} deg")
            print(f"      R = {cart.r:.3f} deg")

        if joints._instance:
            print(f"    Joints:")
            print(f"      J1 = {joints.j1:.3f} deg")
            print(f"      J2 = {joints.j2:.3f} deg")
            print(f"      J3 = {joints.j3:.3f} deg")
            print(f"      J4 = {joints.j4:.3f} deg")
            print(f"      J5 = {joints.j5:.3f} deg")
            print(f"      J6 = {joints.j6:.3f} deg")

        if not cart._instance and not joints._instance:
            print("    Position register not set to a value.")

        # Ask for write mode
        mode = input("\n  Write as (c)artesian or (j)oint? [c/j]: ").strip().lower()
        if mode not in ('c', 'j'):
            print("  Invalid choice.")
            continue

        try:
            if mode == 'c':
                # Cartesian input
                print("  Enter Cartesian values (press Enter to keep current value):")
                x = input_float("X (mm)", cart.x if cart._instance else None)
                y = input_float("Y (mm)", cart.y if cart._instance else None)
                z = input_float("Z (mm)", cart.z if cart._instance else None)
                w = input_float("W (deg)", cart.w if cart._instance else None)
                p = input_float("P (deg)", cart.p if cart._instance else None)
                r = input_float("R (deg)", cart.r if cart._instance else None)

                new_cart = CartesianPosition(x, y, z, w, p, r, None)
                robot.snpx.position_registers.write(pr_num, new_cart)

            else:
                # Joint input
                print("  Enter Joint values (press Enter to keep current value):")
                j1 = input_float("J1 (deg)", joints.j1 if joints._instance else None)
                j2 = input_float("J2 (deg)", joints.j2 if joints._instance else None)
                j3 = input_float("J3 (deg)", joints.j3 if joints._instance else None)
                j4 = input_float("J4 (deg)", joints.j4 if joints._instance else None)
                j5 = input_float("J5 (deg)", joints.j5 if joints._instance else None)
                j6 = input_float("J6 (deg)", joints.j6 if joints._instance else None)

                new_joints = JointsPosition(j1, j2, j3, j4, j5, j6, 0, 0, 0)
                robot.snpx.position_registers._instance.Write(pr_num, new_joints._instance)

        except ValueError:
            print("  Invalid value entered.")
            continue

        # Read back to confirm
        updated = robot.snpx.position_registers.read(pr_num)
        updated_cart = updated.cartesian_position
        updated_joints = updated.joints_position

        print(f"\n  PR[{pr_num}] updated value:")
        if updated_cart._instance:
            print(f"    Cartesian:")
            print(f"      X = {updated_cart.x:.3f} mm")
            print(f"      Y = {updated_cart.y:.3f} mm")
            print(f"      Z = {updated_cart.z:.3f} mm")
            print(f"      W = {updated_cart.w:.3f} deg")
            print(f"      P = {updated_cart.p:.3f} deg")
            print(f"      R = {updated_cart.r:.3f} deg")

        if updated_joints._instance:
            print(f"    Joints:")
            print(f"      J1 = {updated_joints.j1:.3f} deg")
            print(f"      J2 = {updated_joints.j2:.3f} deg")
            print(f"      J3 = {updated_joints.j3:.3f} deg")
            print(f"      J4 = {updated_joints.j4:.3f} deg")
            print(f"      J5 = {updated_joints.j5:.3f} deg")
            print(f"      J6 = {updated_joints.j6:.3f} deg")
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
