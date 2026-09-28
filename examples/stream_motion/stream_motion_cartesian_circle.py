"""
Stream Motion - Cartesian Circle
=================================
Draw a horizontal circle that starts and ends at the current position of the robot.
Positions are the flange in the world frame: on some controllers (CRX), select a tool frame
equal to zero first. Run on the robot a TP program with IBGN start[1] and IBGN end[1].
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Stream Motion: Cartesian Circle")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    radius_str = input("Circle radius in mm (default 20): ").strip()
    radius = float(radius_str) if radius_str else 20.0
    speed_str = input("Speed in mm/s (default 50): ").strip()
    speed = float(speed_str) if speed_str else 50.0

    sm.start_monitoring()
    print("\nStart the TP program with IBGN start[1] on the robot...")
    if not sm.wait_for_ready(60000):
        raise SystemExit("The program did not reach IBGN start.")

    # Prudent Cartesian limits: the joint limits cannot be checked for Cartesian positions
    limits = CartesianLimits(250, 500, 2500, 30, 90, 450)
    planner = MotionPlanner(sm.joint_limits, limits)

    # Circle in a horizontal plane, centered at 'radius' mm along -X from the current position
    start = sm.queue_end_cartesian_position
    plane = XYZWPRPosition(start.x - radius, start.y, start.z, 0, 0, 0)
    trajectory = planner.create_cartesian_path(FanucMotion.to_cartesian_pose(start)) \
        .add_circle(FanucMotion.to_cartesian_pose(plane), radius, speed, FanucMotion.fine()) \
        .build()

    report = trajectory.check_cartesian(limits, sm.cycle_time)
    print(f"Duration: {trajectory.duration:.2f} s, max speed: {report.max_linear_velocity:.1f} mm/s")

    completed = sm.wait_for_motion(sm.enqueue(trajectory), 120000)
    print(f"Motion completed: {completed}")
    print(f"Session finished: {sm.finish(10000)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
