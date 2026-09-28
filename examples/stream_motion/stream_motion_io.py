"""
Stream Motion - I/O During Motion
==================================
Read DI[1] to DI[16] during a session, and switch DO[1] ON in the middle of a motion,
exactly when the robot reaches the first position.
Run on the robot a TP program with IBGN start[1] and IBGN end[1], in AUTO mode at 100% override.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.robotics.motion.motion_planner import MotionPlanner

print("=" * 60)
print("  FANUC SDK - Stream Motion: I/O During Motion")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    sm.start_monitoring()

    # Range of 16 inputs read with the positions sent
    sm.add_io_monitor(IOType.DI, 1)

    print("\nStart the TP program with IBGN start[1] on the robot...")
    if not sm.wait_for_ready(60000):
        raise SystemExit("The program did not reach IBGN start.")

    # J1 +10 degrees, DO[1] ON, then back and DO[1] OFF
    start = sm.queue_end_joint_position
    values = list(start.values)
    values[0] += 10
    planner = MotionPlanner(sm.joint_limits, None)
    trajectory = planner.create_joint_path(FanucMotion.to_joint_values(start)) \
        .move_joint(FanucMotion.to_joint_values(JointsPosition(*values)), 20, FanucMotion.fine()) \
        .set_io(FanucMotion.signal(IOType.DO, 1), True) \
        .move_joint(FanucMotion.to_joint_values(start), 20, FanucMotion.fine()) \
        .set_io(FanucMotion.signal(IOType.DO, 1), False) \
        .build()
    sm.wait_for_motion(sm.enqueue(trajectory), 60000)

    for io_range in sm.io_values:
        print(f"{io_range.type.name}[{io_range.index}..{io_range.index + 15}] = {io_range.value:016b} (read {io_range.age} cycles ago)")
    print(f"DI[1] = {sm.get_io(IOType.DI, 1)}")

    print(f"Session finished: {sm.finish(10000)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
