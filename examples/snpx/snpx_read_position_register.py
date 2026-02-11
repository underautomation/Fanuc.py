"""
SNPX - Read Position Register
===============================
Read a position register (PR[i]) from the robot via SNPX protocol.
Shows both Cartesian and joint representations.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - SNPX: Read Position Register")
print("=" * 60)

# Connect with SNPX enabled
robot = connect_robot(enable_snpx=True)

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

        # Read position register via SNPX
        position = robot.snpx.position_registers.read(pr_num)

        print(f"\n  PR[{pr_num}]:")
        print(f"    User frame: {position.user_frame}")
        print(f"    User tool : {position.user_tool}")

        # Cartesian coordinates
        cart = position.cartesian_position

        if cart._instance:
            print(f"    Cartesian:")
            print(f"      X = {cart.x:.3f} mm")
            print(f"      Y = {cart.y:.3f} mm")
            print(f"      Z = {cart.z:.3f} mm")
            print(f"      W = {cart.w:.3f} deg")
            print(f"      P = {cart.p:.3f} deg")
            print(f"      R = {cart.r:.3f} deg")

        # Joint coordinates
        joints = position.joints_position
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
        print()
finally:
    robot.disconnect()
    print("Disconnected.")
