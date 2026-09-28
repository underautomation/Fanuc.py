"""
Motion - Plan a Joint Path
===========================
Plan joint motions as in a TP program (J, CNT, FINE), then read the duration,
some positions, and the velocity, acceleration and jerk of each axis.
Offline: no robot connection needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Motion: Plan a Joint Path")
print("=" * 60)

# Limits of each axis (example values). On a robot, read them with robot.stream_motion.read_limits()
limits = JointLimits(
    [120, 120, 180, 180, 180, 180],
    [300, 300, 450, 675, 675, 675],
    [1125, 1125, 1687, 2530, 1265, 2530])
planner = MotionPlanner(limits, None)

home = JointValues([0, 0, 0, 0, -90, 0])
p1 = JointValues([40, 10, -10, 0, -80, 0])
p2 = JointValues([40, 30, -20, 20, -60, 45])

for name, termination in (("FINE", FanucMotion.fine()), ("CNT100", FanucMotion.cnt(100))):
    trajectory = planner.create_joint_path(home) \
        .move_joint(p1, 80, termination) \
        .move_joint(p2, 80, termination) \
        .move_joint(home, 80, FanucMotion.fine()) \
        .build()
    print(f"\nWith {name} between the motions: {trajectory.duration:.3f} s")

# Positions along the last trajectory
print("\nJ1 and J2 every 0.25 s:")
t = 0.0
while t <= trajectory.duration:
    p = trajectory.get_joints(t).values
    print(f"  t = {t:5.2f} s   J1 = {p[0]:7.2f}   J2 = {p[1]:7.2f}")
    t += 0.25

# FANUC joint position, when needed
end = FanucMotion.to_joints_position(trajectory.get_joints(trajectory.duration))
print(f"\nEnd: J1 = {end.j1:.2f}, J5 = {end.j5:.2f}")

# Maximum values, computed as the robot does at 8 ms
report = trajectory.check(limits, 0.008, False)
print(f"\nValid: {report.is_valid}")
for axis in range(6):
    print(f"  J{axis + 1}: {report.max_velocity[axis]:7.1f} deg/s  {report.max_acceleration[axis]:7.1f} deg/s2  "
          f"{report.max_jerk[axis]:8.1f} deg/s3")
