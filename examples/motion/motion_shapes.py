"""
Motion - Shapes and Splines
============================
Create a circle, a rounded rectangle, a helix and a spline through points,
and display the duration and the maximum speed of each trajectory.
Offline: no robot connection needed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Motion: Shapes and Splines")
print("=" * 60)

limits = CartesianLimits(500, 2000, 10000, 90, 360, 1800)
planner = MotionPlanner(None, limits)


def wpr(x, y, z, w, p, r):
    """FANUC position X, Y, Z, W, P, R as a pose of the planner"""
    return FanucMotion.to_cartesian_pose(XYZWPRPosition(x, y, z, w, p, r))


start = wpr(650, 0, 300, 180, 0, 0)
plane = wpr(600, 0, 300, 0, 0, 0)   # center of the shapes, horizontal plane


def show(name, trajectory):
    report = trajectory.check_cartesian(limits, 0.008)
    end = FanucMotion.sample_cartesian(trajectory, 0.008)[-1]
    print(f"\n{name}")
    print(f"  Duration: {trajectory.duration:.2f} s, max speed: {report.max_linear_velocity:.1f} mm/s, valid: {report.is_valid}")
    print(f"  End: X={end.x:.1f} Y={end.y:.1f} Z={end.z:.1f} W={end.w:.1f}")


show("Circle, radius 50 mm, 200 mm/s",
     planner.create_cartesian_path(start).add_circle(plane, 50, 200, FanucMotion.fine()).build())

show("Rectangle 100 x 60 mm, corners of radius 10 mm, 200 mm/s",
     planner.create_cartesian_path(start).add_rectangle(plane, 100, 60, 10, 200, FanucMotion.fine()).build())

show("Helix, radius 20 mm, 10 mm up per turn, 3 turns, 100 mm/s",
     planner.create_cartesian_path(start).add_helix(plane, 20, 10, 3, 100, FanucMotion.fine()).build())

points = [
    wpr(700, 40, 300, 180, 0, 0),
    wpr(750, 0, 320, 180, 10, 0),
    wpr(800, -40, 300, 180, 0, 20),
]
show("Spline through 3 points, 150 mm/s",
     planner.create_cartesian_path(start).move_spline(points, 150, FanucMotion.fine()).build())
