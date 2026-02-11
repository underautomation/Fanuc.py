"""
Telnet - Get Current Position
=============================
Read the current Cartesian position (X, Y, Z, W, P, R) of the robot
via the Telnet KCL protocol.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Telnet: Get Current Position")
print("=" * 60)

# Connect with Telnet enabled
robot = connect_robot(enable_telnet=True)

try:
    result = robot.telnet.get_current_pose()

    if result.succeed:
        pos = result.position
        print(f"\nCurrent robot position (Group {result.group}):")
        print(f"  X = {pos.x:.3f} mm")
        print(f"  Y = {pos.y:.3f} mm")
        print(f"  Z = {pos.z:.3f} mm")
        print(f"  W = {pos.w:.3f} deg")
        print(f"  P = {pos.p:.3f} deg")
        print(f"  R = {pos.r:.3f} deg")
        print(f"  Config: {pos.configuration}")
    else:
        print(f"\nError: {result.error_text}")
finally:
    robot.disconnect()
    print("\nDisconnected.")
