"""
Stream Motion - Joint Motion
=============================
Move J1 back and forth with a smooth trajectory planned within the limits of the robot.
Run on the robot a TP program with IBGN start[1] and IBGN end[1], in AUTO mode at 100% override.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Stream Motion: Joint Motion")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    amplitude_str = input("J1 amplitude in degrees (default 10): ").strip()
    amplitude = float(amplitude_str) if amplitude_str else 10.0
    speed_str = input("Speed in % of the velocity limits (default 20): ").strip()
    speed = float(speed_str) if speed_str else 20.0

    # Read the limits and start the status output (before running the TP program)
    sm.start_monitoring()
    print(f"\nCommunication cycle: {sm.cycle_time * 1000:.1f} ms")

    print("Start the TP program with IBGN start[1] on the robot...")
    if not sm.wait_for_ready(60000):
        raise SystemExit("The program did not reach IBGN start.")

    # J1 goes to +amplitude, then -amplitude, then back, with smooth corners (CNT100)
    start = sm.queue_end_joint_position
    values = list(start.values)
    values[0] = start.j1 + amplitude
    left = JointsPosition(*values)
    values[0] = start.j1 - amplitude
    right = JointsPosition(*values)

    # The planner uses its own position type: FanucMotion converts the FANUC positions
    planner = MotionPlanner(sm.joint_limits, None)
    trajectory = planner.create_joint_path(FanucMotion.to_joint_values(start)) \
        .move_joint(FanucMotion.to_joint_values(left), speed, FanucMotion.cnt(100)) \
        .move_joint(FanucMotion.to_joint_values(right), speed, FanucMotion.cnt(100)) \
        .move_joint(FanucMotion.to_joint_values(start), speed, FanucMotion.fine()) \
        .build()
    print(f"Trajectory duration: {trajectory.duration:.2f} s")

    motion_id = sm.enqueue(trajectory)
    completed = sm.wait_for_motion(motion_id, 120000)
    print(f"Motion completed: {completed}")

    # The TP program continues after IBGN end
    print(f"Session finished: {sm.finish(10000)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
