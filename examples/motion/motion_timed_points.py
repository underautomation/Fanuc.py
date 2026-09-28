"""
Motion - Timed Points, Check and Retime
========================================
Create a trajectory that passes through joint positions at given times,
check it against the limits of the robot, and slow it down when it is too fast.
Offline: no robot connection needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import underautomation.fanuc  # loads the library
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.trajectory import Trajectory

print("=" * 60)
print("  FANUC SDK - Motion: Timed Points, Check and Retime")
print("=" * 60)

limits = JointLimits(
    [120, 120, 180, 180, 180, 180],
    [300, 300, 450, 675, 675, 675],
    [1125, 1125, 1687, 2530, 1265, 2530])

points = [
    JointValues([0, 0, 0, 0, -90, 0]),
    JointValues([30, 10, 0, 0, -90, 0]),
    JointValues([60, 0, 10, 0, -80, 0]),
    JointValues([90, -10, 10, 0, -80, 30]),
]
times = [0.0, 0.4, 0.8, 1.2]   # too fast on purpose

trajectory = Trajectory.from_timed_joints(points, times)
print(f"\nDuration: {trajectory.duration:.2f} s")
for i, time in enumerate(times):
    j1 = trajectory.get_joints(time).values[0]
    print(f"  t = {time:.1f} s: J1 = {j1:.2f} (point {i + 1}: {points[i].values[0]:.2f})")

cycle = 0.008
report = trajectory.check(limits, cycle, True)
print(f"\nValid: {report.is_valid}, {report.violation_count} limit(s) exceeded")
for violation in report.violations[:5]:
    print(f"  {violation}")

if not report.is_valid:
    # Same path, played slower. True: checked in single precision, as with protocol version 1.
    slower = trajectory.retime(limits, cycle, True)
    print(f"\nRetimed: {slower.duration:.2f} s instead of {trajectory.duration:.2f} s, "
          f"valid: {slower.check(limits, cycle, True).is_valid}")
