"""
Motion - Frames and Quaternions
================================
Convert W, P, R angles to quaternions, interpolate between two orientations,
and convert a position between flange, tool, user frame and world frame.
Offline: no robot connection needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.fanuc.common.quaternion import Quaternion
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition

print("=" * 60)
print("  FANUC SDK - Motion: Frames and Quaternions")
print("=" * 60)

# Orientations
a = XYZWPRPosition(0, 0, 0, 180, 0, 0)
b = XYZWPRPosition(0, 0, 0, 180, 40, 30)
qa = a.get_quaternion()
qb = b.get_quaternion()
print(f"\nQuaternion of W=180 P=0 R=0: {qa}")
print(f"Angle between the two orientations: {qa.angle_to(qb):.2f} deg")

middle = XYZWPRPosition(0, 0, 0, 0, 0, 0)
middle.set_quaternion(Quaternion.slerp(qa, qb, 0.5))
print(f"Half way: W={middle.w:.2f} P={middle.p:.2f} R={middle.r:.2f}")

# Frames
tool = XYZWPRPosition(0, 0, 150, 0, 0, 0)            # tool frame, relative to the flange
user_frame = XYZWPRPosition(800, -200, 0, 0, 0, 90)  # user frame, relative to the world frame
flange = XYZWPRPosition(700, 0, 400, 180, 0, 0)      # flange in the world frame

tcp = flange.flange_to_tcp(tool)
print(f"\nTool center point in the world frame: X={tcp.x:.1f} Y={tcp.y:.1f} Z={tcp.z:.1f}")

tcp_user = tcp.world_to_user_frame(user_frame)
print(f"Tool center point in the user frame:  X={tcp_user.x:.1f} Y={tcp_user.y:.1f} Z={tcp_user.z:.1f} R={tcp_user.r:.1f}")

back = tcp_user.user_frame_to_world(user_frame).tcp_to_flange(tool)
print(f"Back to the flange:                   X={back.x:.1f} Y={back.y:.1f} Z={back.z:.1f}")
