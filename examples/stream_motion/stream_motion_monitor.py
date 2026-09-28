"""
Stream Motion - Monitor the Robot
==================================
Start the Stream Motion status output, read the limits of the robot,
and display its position and state for a few seconds. The robot does not move.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot

print("=" * 60)
print("  FANUC SDK - Stream Motion: Monitor the Robot")
print("=" * 60)

robot = connect_robot(enable_stream_motion=True)
sm = robot.stream_motion

try:
    # Reads the limits of the robot, starts the status output and measures the communication cycle
    sm.start_monitoring()
    print(f"\nProtocol version: {sm.protocol_version}")
    print(f"Communication cycle: {sm.cycle_time * 1000:.1f} ms")

    limits = sm.limits
    if limits is not None:
        reference = limits.reference_limits
        print(f"\nReference limits ({limits.axis_count} axes):")
        for axis in range(limits.axis_count):
            print(f"  J{axis + 1}: {reference.velocity[axis]:8.1f} deg/s  "
                  f"{reference.acceleration[axis]:8.1f} deg/s2  {reference.jerk[axis]:9.1f} deg/s3")

    print("\nStatus during 5 seconds:")
    for _ in range(10):
        status = sm.last_status
        joints = status.joint_position
        print(f"  State: {sm.state.name}  J1..J6: {joints.j1:.2f} {joints.j2:.2f} {joints.j3:.2f} "
              f"{joints.j4:.2f} {joints.j5:.2f} {joints.j6:.2f}  moving: {status.is_moving}")
        time.sleep(0.5)

    statistics = sm.statistics
    print(f"\nStatus received: {statistics.status_count}, lost: {statistics.lost_status_count}")

    sm.stop_monitoring()

finally:
    robot.disconnect()
    print("\nDisconnected.")
