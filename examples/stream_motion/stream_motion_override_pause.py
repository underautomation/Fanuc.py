"""
Stream Motion - Override, Pause and Abort
==========================================
Start a slow J1 motion, then change the override, pause and resume it,
and finally abort it. The robot always stops smoothly on its path.
Run on the robot a TP program with IBGN start[1] and IBGN end[1], in AUTO mode at 100% override.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Stream Motion: Override, Pause and Abort")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    sm.start_monitoring()
    print("\nStart the TP program with IBGN start[1] on the robot...")
    if not sm.wait_for_ready(60000):
        raise SystemExit("The program did not reach IBGN start.")

    # J1 +30 degrees at 5% speed
    start = sm.queue_end_joint_position
    values = list(start.values)
    values[0] += 30
    planner = MotionPlanner(sm.joint_limits, None)
    sm.enqueue(planner.create_joint_path(FanucMotion.to_joint_values(start))
               .move_joint(FanucMotion.to_joint_values(JointsPosition(*values)), 5, FanucMotion.fine()).build())

    time.sleep(1)
    print("Override 50%")
    sm.override = 50
    time.sleep(2)

    print("Pause")
    sm.pause()
    time.sleep(2)
    print(f"  J1 = {sm.last_status.joint_position.j1:.2f}, moving: {sm.last_status.is_moving}")

    print("Resume at 100%")
    sm.override = 100
    sm.resume()
    time.sleep(1)

    print("Abort: the robot stops on its path and the queue is cancelled")
    sm.abort()
    sm.wait_for_idle(10000)
    print(f"  Stopped at J1 = {sm.last_status.joint_position.j1:.2f}")

    # Go back to the start from the stop position
    back = planner.create_joint_path(FanucMotion.to_joint_values(sm.queue_end_joint_position)) \
        .move_joint(FanucMotion.to_joint_values(start), 20, FanucMotion.fine()).build()
    sm.wait_for_motion(sm.enqueue(back), 60000)
    print(f"Session finished: {sm.finish(10000)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
