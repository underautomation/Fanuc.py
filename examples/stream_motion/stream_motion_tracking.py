"""
Stream Motion - Target Tracking
================================
The robot follows a target that you type: enter an offset for J1 and the robot goes there
smoothly, even if you change the target during the motion.
Run on the robot a TP program with IBGN start[1] and IBGN end[1], in AUTO mode at 100% override.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.robotics.motion.position_format import PositionFormat

print("=" * 60)
print("  FANUC SDK - Stream Motion: Target Tracking")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    sm.start_monitoring()
    print("\nStart the TP program with IBGN start[1] on the robot...")
    if not sm.wait_for_ready(60000):
        raise SystemExit("The program did not reach IBGN start.")

    # The robot follows the target at 20% of its velocity limits
    start = sm.queue_end_joint_position
    sm.start_tracking(PositionFormat.Joint, 20)

    while True:
        text = input("\nJ1 offset in degrees from the start (-15 to 15, empty to stop): ").strip()
        if not text:
            break
        offset = max(-15.0, min(15.0, float(text)))
        values = list(start.values)
        values[0] = start.j1 + offset
        sm.set_joint_tracking_target(JointsPosition(*values))
        print(f"Target J1 = {values[0]:.2f}")

    # Back to the start, then stop the tracking
    sm.set_joint_tracking_target(start)
    sm.wait_for_idle(30000)
    sm.stop_tracking()
    print(f"Session finished: {sm.finish(10000)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
