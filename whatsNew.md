## Stream Motion (J519): new API

> **Breaking change:** the Stream Motion API was rewritten. You do not build and send packets anymore. The SDK synchronizes the positions with the status of the robot, sends a few positions in advance, and stops the robot smoothly when your application stops giving positions. Code written for the previous API must be updated (see "How to migrate" below).

The client (`robot.stream_motion`, or `StreamMotionClient` alone) gives three ways to move the robot:

- **Queue of trajectories:** plan a trajectory with the new motion planner and call `enqueue()`. It returns an id for `wait_for_motion()`. `wait_for_idle()` waits for the whole queue. Control the motion with `override`, `pause()`, `resume()` and `abort()`.
- **Target tracking:** call `start_tracking()`, then change the target at any time with `set_joint_tracking_target()` or `set_cartesian_tracking_target()`.
- **Callback streaming:** call `start_callback_streaming()`, then give each position in the `setpoint_requested` event with `e.set_joints()`, `e.set_cartesian()` or `e.hold()`. With Python, the timing of the callback depends on the interpreter: prefer target tracking.

```python
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.robotics.motion.motion_planner import MotionPlanner

robot = FanucRobot()
parameters = ConnectionParameters("192.168.0.1")
parameters.stream_motion.enable = True
robot.connect(parameters)
sm = robot.stream_motion

# Read the limits of the robot, start the status output and measure the communication cycle
sm.start_monitoring()

# J1 +10 degrees then back, at 20% of the velocity limits
start = sm.queue_end_joint_position
values = list(start.values)
values[0] += 10
target = JointsPosition(*values)
planner = MotionPlanner(sm.joint_limits, None)
trajectory = planner.create_joint_path(FanucMotion.to_joint_values(start)) \
    .move_joint(FanucMotion.to_joint_values(target), 20, FanucMotion.cnt(100)) \
    .move_joint(FanucMotion.to_joint_values(start), 20, FanucMotion.fine()) \
    .build()

# The motion starts when the TP program reaches IBGN start
sm.wait_for_motion(sm.enqueue(trajectory), 60000)

# Release the TP program: it continues after IBGN end
sm.finish(10000)
```

```python
from underautomation.robotics.motion.position_format import PositionFormat

# Follow a target that can change at any time, at 30% of the velocity limits
sm.start_tracking(PositionFormat.Joint, 30)
values = list(start.values)
values[0] = start.j1 + 10
sm.set_joint_tracking_target(JointsPosition(*values))
sm.wait_for_idle(10000)
sm.stop_tracking()
```

Other new features:

- Protocol versions 1, 2 and 3 with `parameters.stream_motion.protocol_version` (default 1, must not be higher than `$STMO.$USABLE_VER`). Version 2 sends joint positions in double precision.
- New connection settings: `buffer_lead_time` (0.024 s), `packet_stack_size` (10), `status_timeout_ms` (1000 ms) and `high_priority` (True). `port` is still 60015.
- `state` gives the state of the client: `Disconnected`, `Connected`, `Monitoring`, `Ready`, `Streaming` or `Finishing`. `wait_for_ready()` waits until the TP program reaches `IBGN start`.
- `last_status` and the `status_received` event give the joint and Cartesian positions, the motor currents and the flags of the robot (`is_waiting_for_command`, `is_moving`...). `cycle_time` gives the measured communication cycle and `statistics` the quality of the communication.
- New events: `session_started`, `session_ended` (with a `SessionEndReason`), `motion_completed`, `underrun` and `error_occurred`. Subscribe with `sm.session_ended(handler)`. Errors are raised as `StreamMotionException`, with a `StreamMotionError` code.
- A session uses only one format, joint or Cartesian: call `finish()` to use the other format in the next session. `has_active_format` and `active_format` give the current format.
- `read_limits()` reads the velocity, acceleration and jerk limits of each axis. `reference_limits` are always safe, `compute_limits()` gives the limits for a flange speed and a payload, and `get_table()` gives the raw table of one axis.
- I/O synchronized with the motion: `add_io_monitor()` reads ranges of 16 I/O, `get_io()` and `io_values` give their values, `write_io()` and `write_io_group()` write outputs, and `io_anticipation` compensates the delay of the robot. An output can also be switched at a precise time of a trajectory.
- `features.has_stream_motion` tells if the J519 option is installed on the robot.

**How to migrate:**

| Previous API                                                                   | New API                                                                                                                      |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `start()` / `stop()`                                                           | `start_monitoring()` / `stop_monitoring()`                                                                                   |
| `send_joint_command()`, `send_cartesian_command()`, `send_command()` in a loop | `enqueue()` a `Trajectory`, follow a target with `start_tracking()`, or give each position with `start_callback_streaming()` |
| `isLastData=True`                                                              | `finish()`                                                                                                                   |
| `state_received` event, `last_state`                                           | `status_received` event, `last_status`                                                                                       |
| `receive_error` event                                                          | `error_occurred` event                                                                                                       |
| `request_threshold()`                                                          | `read_limits()`                                                                                                              |
| `is_streaming`                                                                 | `state == StreamMotionState.Streaming`                                                                                       |
| `robot_frequency`, `measured_frequency`                                        | `cycle_time`                                                                                                                 |
| `packet_count`                                                                 | `statistics`                                                                                                                 |
| `send_timeout_ms`, `receive_timeout_ms`                                        | `status_timeout_ms`                                                                                                          |
| `StreamMotionClient.connect(ip, port, sendTimeoutMs, receiveTimeoutMs)`        | `StreamMotionClient.connect(ip, parameters)` with a `StreamMotionConnectParameters`                                          |

The types `CommandPacket`, `StatePacket`, `MotionData`, `DataStyle`, `RobotStatus`, `AckPacket`, `ThresholdType`, `IOReadResult`, `StateReceivedEventArgs` and `ReceiveErrorEventArgs` were removed.

Documentation: [Stream Motion](https://underautomation.com/fanuc/documentation/stream-motion)

## New motion planner

The new module `underautomation.robotics.motion` creates smooth trajectories that respect velocity, acceleration and jerk limits. It works offline, without robot. Trajectories can be sent with Stream Motion, used in a simulation, or checked before use.

The `underautomation.robotics` modules are common to all UnderAutomation robot SDKs: the same code plans trajectories for other robot brands. The FANUC specific part is the `FanucMotion` class of `underautomation.fanuc.motion.fanuc_motion`: it converts `JointsPosition` and `XYZWPRPosition`, gives the FINE, CNT and CR terminations and the I/O signals, and returns the FANUC positions of a trajectory.

- `JointLimits` (velocity, acceleration and jerk of 9 axes) and `CartesianLimits` (linear and angular velocity, acceleration and jerk). On a robot, read the joint limits with `robot.stream_motion.read_limits().reference_limits`.
- `MotionPlanner` creates joint and Cartesian paths. With `tool_frame` and `user_frame`, targets are tool positions in this user frame.
- Positions of the planner: `JointValues` and `CartesianPose` (x, y, z, `orientation` and external axes). `Orientation` converts from and to quaternions, Euler angles (`EulerConvention`), rotation vectors and rotation matrices. The W, P, R angles of FANUC are `EulerConvention.FixedXYZ`.
- Joint paths: `move_joint()` (speed in %, termination, optional acceleration in %), `move_joint_time()`, `move_joint_spline()`, `wait()` and `set_io()`.
- Cartesian paths: `move_linear()`, `move_circular()`, `move_linear_time()`, `move_spline()`, and shapes in any plane: `add_circle()`, `add_rectangle()`, `add_polygon()`, `add_helix()` and `add_spiral()`.
- Terminations as in a TP program: `FanucMotion.fine()`, `FanucMotion.cnt(0..100)` and `FanucMotion.cr(distance_mm)`.
- All motions use jerk limited profiles. The profile is also available alone with `DoubleSProfile`.

```python
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.motion.fanuc_motion import FanucMotion
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.robotics.motion.motion_planner import MotionPlanner

joint_limits = JointLimits(
    [120, 120, 180, 180, 180, 180],         # velocity, deg/s
    [300, 300, 450, 675, 675, 675],         # acceleration, deg/s2
    [1125, 1125, 1687, 2530, 1265, 2530])   # jerk, deg/s3
cartesian_limits = CartesianLimits(500, 2000, 10000, 90, 360, 1800)
planner = MotionPlanner(joint_limits, cartesian_limits)

# J P[1] 100% CNT50, J P[2] 30% FINE ACC50, DO[1]=ON, WAIT 0.5 s, then back in 2 s
start = JointValues([0, 0, 0, 0, -90, 0])
joint = planner.create_joint_path(start) \
    .move_joint(JointValues([40, 0, 0, 0, -90, 0]), 100, FanucMotion.cnt(50)) \
    .move_joint(JointValues([40, 30, -20, 0, -60, 0]), 30, FanucMotion.fine(), 50) \
    .set_io(FanucMotion.signal(IOType.DO, 1), True) \
    .wait(0.5) \
    .move_joint_time(start, 2.0, FanucMotion.fine()) \
    .build()

# L 200mm/sec CR10, then C at 150mm/sec FINE
def wpr(x, y, z, w, p, r):
    return FanucMotion.to_cartesian_pose(XYZWPRPosition(x, y, z, w, p, r))

cartesian = planner.create_cartesian_path(wpr(500, 0, 300, 180, 0, 0)) \
    .move_linear(wpr(600, 0, 300, 180, 0, 0), 200, FanucMotion.cr(10)) \
    .move_circular(wpr(550, 150, 300, 180, 0, 0), wpr(500, 100, 300, 180, 0, 30), 150, FanucMotion.fine()) \
    .build()

# FANUC positions of the trajectory, one per 8 ms, with continuous W, P, R
positions = FanucMotion.sample_cartesian(cartesian, 0.008)
```

A `Trajectory` gives its `duration`, the position at any time (`get_joints()`, `get_cartesian()`), samples at a fixed period (`sample_joints()`, `sample_cartesian()`) and its I/O events (`io_events`, `add_io_event()`). Trajectories can also be created from your own positions:

- `Trajectory.from_joint_samples()` and `FanucMotion.from_cartesian_samples()`: one position per communication cycle, sent without any change.
- `Trajectory.from_timed_joints()` and `Trajectory.from_timed_cartesian()`: a few positions with their time.
- `check()` and `check_cartesian()` compute the velocity, acceleration and jerk as the robot does and return a report. `retime()` and `retime_cartesian()` play the same path slower so that the limits are respected (with the last parameter set to `True`, also after the rounding of protocol version 1).

```python
from underautomation.robotics.motion.trajectory import Trajectory

trajectory = Trajectory.from_timed_joints(
    [JointValues([0, 0, 0, 0, -90, 0]), JointValues([90, 0, 0, 0, -90, 0])],
    [0.0, 0.5])

report = trajectory.check(joint_limits, 0.008, True)
if not report.is_valid:
    trajectory = trajectory.retime(joint_limits, 0.008, True)

samples = trajectory.sample_joints(0.008)
```

Documentation: [Motion planner](https://underautomation.com/fanuc/documentation/motion)

## Quaternions and frame operations

New `Quaternion` class (`qw`, `qx`, `qy`, `qz`) with `slerp()`, `angle_to()`, `from_axis_angle()`, `to_axis_angle()`, `from_rotation_matrix()`, `to_rotation_matrix()`, `multiply()`, `conjugate()` and `normalize()`.

New methods on `XYZWPRPosition`, so also on `CartesianPosition`: `get_quaternion()`, `set_quaternion()`, `multiply()`, `inverse()`, `flange_to_tcp()`, `tcp_to_flange()`, `user_frame_to_world()` and `world_to_user_frame()`.

`to_homogeneous_matrix()` moved from `CartesianPosition` to its base class `XYZWPRPosition`. Existing code still works.

```python
from underautomation.fanuc.common.quaternion import Quaternion
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition

tool = XYZWPRPosition(0, 0, 150, 0, 0, 0)            # tool frame, relative to the flange
user_frame = XYZWPRPosition(800, -200, 0, 0, 0, 90)  # user frame, relative to the world frame
flange = XYZWPRPosition(700, 0, 400, 180, 0, 0)      # flange in the world frame

tcp_in_user_frame = flange.flange_to_tcp(tool).world_to_user_frame(user_frame)

a = XYZWPRPosition(0, 0, 0, 180, 0, 0).get_quaternion()
b = XYZWPRPosition(0, 0, 0, 180, 30, 0).get_quaternion()
half_way = Quaternion.slerp(a, b, 0.5)
angle = a.angle_to(b)  # 30 degrees
```

Documentation: [Frames & orientations](https://underautomation.com/fanuc/documentation/motion-frames-orientations)
