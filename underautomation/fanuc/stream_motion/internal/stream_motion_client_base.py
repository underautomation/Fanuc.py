from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.data.stream_motion_state import StreamMotionState
from underautomation.fanuc.stream_motion.data.stream_motion_status import StreamMotionStatus
from underautomation.fanuc.stream_motion.data.stream_motion_statistics import StreamMotionStatistics
from underautomation.fanuc.stream_motion.data.stream_motion_limits import StreamMotionLimits
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.robotics.motion.position_format import PositionFormat
from underautomation.robotics.motion.trajectory import Trajectory
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.fanuc.stream_motion.data.io_value import IOValue
from underautomation.fanuc.stream_motion.data.status_received_event_args import StatusReceivedEventArgs
from underautomation.fanuc.stream_motion.data.session_event_args import SessionEventArgs
from underautomation.fanuc.stream_motion.data.session_ended_event_args import SessionEndedEventArgs
from underautomation.fanuc.stream_motion.data.motion_event_args import MotionEventArgs
from underautomation.fanuc.stream_motion.data.stream_motion_error_event_args import StreamMotionErrorEventArgs
from underautomation.fanuc.stream_motion.data.setpoint_request_event_args import SetpointRequestEventArgs
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionClientBase as stream_motion_client_base
from UnderAutomation.Fanuc.StreamMotion.Data import StreamMotionState as stream_motion_state
from UnderAutomation.Robotics.Motion import PositionFormat as position_format
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class StreamMotionClientBase:
	'''Stream Motion client (J519 option): real-time control of the robot by sending a position every communication cycle.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_client_base()
		else:
			self._instance = _internal

	def status_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.StatusReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def session_started(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SessionStarted+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def session_ended(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SessionEnded+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def motion_completed(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.MotionCompleted+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def underrun(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.Underrun+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def error_occurred(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ErrorOccurred+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def setpoint_requested(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SetpointRequested+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def disconnect(self) -> None:
		'''Disconnects from the robot. If a session is active, the robot is stopped smoothly and the session is finished first.'''
		self._instance.Disconnect()

	def start_monitoring(self) -> None:
		'''Starts the status output of the robot. The robot then sends its status every communication cycle. The limits of the robot are read first when they are not known yet, and this method returns when the communication cycle is measured.'''
		self._instance.StartMonitoring()

	def stop_monitoring(self) -> None:
		'''Stops the status output of the robot. Not allowed during a session: call finish() first.'''
		self._instance.StopMonitoring()

	def wait_for_ready(self, timeoutMs: int) -> bool:
		'''Waits until a program executes an IBGN start instruction and the robot accepts positions.

		:param timeoutMs: Maximum waiting time in milliseconds
		:returns: True if the robot accepts positions, false after the timeout
		'''
		return self._instance.WaitForReady(timeoutMs)

	def read_limits(self) -> StreamMotionLimits:
		'''Reads the velocity, acceleration and jerk limits of all axes from the robot. The status output is stopped during the reading and started again. Some controllers do not answer while a program waits on an IBGN start instruction: read the limits before. Not allowed during a session.

		:returns: Limits of the robot. They are also stored in limits, and the reference limits in joint_limits.
		'''
		__r = self._instance.ReadLimits()
		return None if __r is None else StreamMotionLimits(__r)

	def enqueue(self, trajectory: Trajectory) -> int:
		'''Adds a trajectory at the end of the queue. The session starts automatically when the robot accepts positions, and the trajectories are sent one after the other, without any change between them.

		:param trajectory: Trajectory to send. It must start at queue_end_joint_position or queue_end_cartesian_position, and trajectories created from samples must use the communication cycle of the robot (cycle_time). Its I/O events must use signals created by signal().
		:returns: Identifier of the motion, to use with wait_for_motion()
		'''
		return self._instance.Enqueue(trajectory._instance if trajectory else None)

	def wait_for_motion(self, motionId: int, timeoutMs: int) -> bool:
		'''Waits until the robot received the last position of a queued trajectory

		:param motionId: Identifier returned by enqueue()
		:param timeoutMs: Maximum waiting time in milliseconds
		:returns: True when the trajectory was completely sent, false after the timeout or if the trajectory was cancelled
		'''
		return self._instance.WaitForMotion(motionId, timeoutMs)

	def wait_for_idle(self, timeoutMs: int) -> bool:
		'''Waits until the queue is empty and the robot does not move. During target tracking, waits until the robot is stopped on the target.

		:param timeoutMs: Maximum waiting time in milliseconds
		:returns: True when idle, false after the timeout
		'''
		return self._instance.WaitForIdle(timeoutMs)

	def finish(self, timeoutMs: int) -> bool:
		'''Finishes the session when the queue is empty and the robot is at rest: the last position is sent with the end flag, and the program continues after the IBGN end instruction. If a program waits on IBGN start without session, it is released at the current position. The callback streaming and the target tracking are stopped first.

		:param timeoutMs: Maximum waiting time in milliseconds
		:returns: True when the session is finished, false after the timeout or if the session ended for another reason
		'''
		return self._instance.Finish(timeoutMs)

	def pause(self) -> None:
		'''Stops smoothly on the path of the current trajectory. The queue is kept and resume() continues the motion. Use it instead of a HOLD, which is not available during Stream Motion.'''
		self._instance.Pause()

	def resume(self) -> None:
		'''Continues the queued trajectories after pause()'''
		self._instance.Resume()

	def abort(self) -> None:
		'''Stops smoothly on the path of the current trajectory, then cancels the current and the queued trajectories. The session stays open and the robot keeps its position. The callback streaming and the target tracking are stopped, and the robot stops as fast as the limits allow.'''
		self._instance.Abort()

	def start_callback_streaming(self, format: PositionFormat) -> None:
		'''Starts to take the positions from the setpoint_requested event instead of the queue. The session starts automatically when the robot accepts positions.

		:param format: Format of the positions given by the event
		'''
		self._instance.StartCallbackStreaming(position_format(int(format)))

	def stop_callback_streaming(self) -> None:
		'''Stops the callback streaming. The last position is kept, and the robot stops smoothly if it was moving.'''
		self._instance.StopCallbackStreaming()

	def start_tracking(self, format: PositionFormat, speedPercent: float=100, accelerationPercent: float=100) -> None:
		'''Starts to follow a target position: the robot goes to the last target given by set_joint_tracking_target() or set_cartesian_tracking_target() as fast as the limits allow, and stops on it. The target can change at any time, even during the motion: the robot then goes smoothly to the new target. The limits are joint_limits in joint format, and cartesian_limits in Cartesian format (the linear and angular limits are shared between X, Y, Z and between the 3 rotation axes). Each axis moves independently, so the path to the target is not a straight line. The first target is the current position. The session starts automatically when the robot accepts positions. The delay between a new target and the start of the motion is about buffer_lead cycles plus the delay of the robot: reduce the buffer lead time of the connection parameters for a faster reaction.

		:param format: Format of the targets
		:param speedPercent: Velocity in percent of the limits (greater than 0, up to 100)
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		self._instance.StartTracking(position_format(int(format)), speedPercent, accelerationPercent)

	def set_joint_tracking_target(self, target: JointsPosition) -> None:
		'''Gives a new joint target to follow (see start_tracking())

		:param target: Target joint position
		'''
		self._instance.SetJointTrackingTarget(target._instance if target else None)

	def set_cartesian_tracking_target(self, target: XYZWPRPosition) -> None:
		'''Gives a new Cartesian target to follow (see start_tracking()). Extended axes are used when the target is an ExtendedCartesianPosition, otherwise they keep their target.

		:param target: Target position, in the frame of the Cartesian positions sent to the robot
		'''
		self._instance.SetCartesianTrackingTarget(target._instance if target else None)

	def stop_tracking(self) -> None:
		'''Stops the target tracking. If the robot was moving, it stops as fast as the limits allow, then it keeps its position.'''
		self._instance.StopTracking()

	def add_io_monitor(self, type: IOType, index: int) -> None:
		'''Adds a range of 16 consecutive I/O to read. Each position sent to the robot reads one range, so several ranges are read one after the other. Values are only read during a session.

		:param type: I/O type
		:param index: Index of the first I/O of the range (starts at 1)
		'''
		self._instance.AddIOMonitor(io_type(int(type)), index)

	def clear_io_monitors(self) -> None:
		'''Removes all ranges of I/O to read'''
		self._instance.ClearIOMonitors()

	def get_io(self, type: IOType, index: int) -> bool:
		'''Returns the last read state of one I/O. The I/O must be in a range added with add_io_monitor(). It returns false while the range was never read.

		:param type: I/O type
		:param index: I/O index
		'''
		return self._instance.GetIO(io_type(int(type)), index)

	def write_io(self, type: IOType, index: int, value: bool) -> None:
		'''Writes one digital I/O with the next position sent to the robot (only during a session)

		:param type: I/O type
		:param index: I/O index (starts at 1)
		:param value: Value to write
		'''
		self._instance.WriteIO(io_type(int(type)), index, value)

	def write_io_group(self, type: IOType, index: int, mask: int, value: int) -> None:
		'''Writes up to 16 consecutive digital I/O with the next position sent to the robot (only during a session)

		:param type: I/O type
		:param index: Index of the first I/O (starts at 1)
		:param mask: Bits of the I/O to write. Bit 0 is the I/O at index.
		:param value: Values of the I/O. Bit 0 is the I/O at index.
		'''
		self._instance.WriteIOGroup(io_type(int(type)), index, mask, value)

	def dispose(self) -> None:
		'''Disconnects and releases the resources'''
		self._instance.Dispose()

	@property
	def ip(self) -> str:
		'''IP address of the robot'''
		return self._instance.Ip

	@property
	def port(self) -> int:
		'''UDP port of the robot'''
		return self._instance.Port

	@property
	def protocol_version(self) -> int:
		'''Protocol version used by this client'''
		return self._instance.ProtocolVersion

	@property
	def connected(self) -> bool:
		'''Indicates whether the client is connected'''
		return self._instance.Connected

	@property
	def state(self) -> StreamMotionState:
		'''Current state of the client'''
		return StreamMotionState(int(self._instance.State))

	@property
	def last_status(self) -> StreamMotionStatus:
		'''Last status received from the robot, or null if no status was received'''
		__r = self._instance.LastStatus
		return None if __r is None else StreamMotionStatus(__r)

	@property
	def cycle_time(self) -> float:
		'''Communication cycle of the robot measured from the status, in seconds (for example 0.008 or 0.002). 0 while it is not known. Trajectories are sampled at this period.'''
		return self._instance.CycleTime

	@property
	def buffer_lead(self) -> int:
		'''Number of positions sent in advance and kept in the robot buffer during the current session'''
		return self._instance.BufferLead

	@property
	def session_count(self) -> int:
		'''Number of sessions started since the connection. A session starts when positions are sent after an IBGN start instruction.'''
		return self._instance.SessionCount

	@property
	def statistics(self) -> StreamMotionStatistics:
		'''Communication statistics since the status output was started'''
		__r = self._instance.Statistics
		return None if __r is None else StreamMotionStatistics(__r)

	@property
	def limits(self) -> StreamMotionLimits:
		'''Limits read from the robot by read_limits() or when the status output starts. Null if they were not read.'''
		__r = self._instance.Limits
		return None if __r is None else StreamMotionLimits(__r)

	@property
	def joint_limits(self) -> JointLimits:
		'''Joint limits used to stop the robot smoothly when the positions stop in joint format. It is set to the reference limits of the robot when the limits are read.'''
		__r = self._instance.JointLimits
		return None if __r is None else JointLimits(None, None, None, __r)

	@joint_limits.setter
	def joint_limits(self, value: JointLimits):
		self._instance.JointLimits = value._instance if value else None

	@property
	def cartesian_limits(self) -> CartesianLimits:
		'''Cartesian limits used to stop the robot smoothly when the positions stop in Cartesian format. When it is null, conservative values are used.'''
		__r = self._instance.CartesianLimits
		return None if __r is None else CartesianLimits(None, None, None, None, None, None, __r)

	@cartesian_limits.setter
	def cartesian_limits(self, value: CartesianLimits):
		self._instance.CartesianLimits = value._instance if value else None

	@property
	def start_tolerance(self) -> float:
		'''Maximum distance between the first position of a trajectory and the position where it starts, in mm or degrees (default 0.01).'''
		return self._instance.StartTolerance

	@start_tolerance.setter
	def start_tolerance(self, value: float):
		self._instance.StartTolerance = value

	@property
	def io_anticipation(self) -> float:
		'''Time in seconds by which the I/O events of trajectories are sent before their position (default 0). It compensates the delay between the reception of a position by the robot and the real motion.'''
		return self._instance.IOAnticipation

	@io_anticipation.setter
	def io_anticipation(self, value: float):
		self._instance.IOAnticipation = value

	@property
	def queue_end_joint_position(self) -> JointsPosition:
		'''Position where the next queued joint trajectory must start: end of the queue, or current position when the queue is empty. Null if no status was received.'''
		__r = self._instance.QueueEndJointPosition
		return None if __r is None else JointsPosition(None, None, None, None, None, None, None, None, None, __r)

	@property
	def queue_end_cartesian_position(self) -> ExtendedCartesianPosition:
		'''Position where the next queued Cartesian trajectory must start: end of the queue, or last position sent when the queue is empty. Before any Cartesian position was sent, it is the Cartesian position of the status (flange center in the world frame by default). Some controllers expect Cartesian positions of the active tool frame: the start of the first trajectory is then not checked. Null if no status was received.'''
		__r = self._instance.QueueEndCartesianPosition
		return None if __r is None else ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, __r)

	@property
	def queued_motion_count(self) -> int:
		'''Number of trajectories waiting or running'''
		return self._instance.QueuedMotionCount

	@property
	def is_callback_streaming(self) -> bool:
		'''Indicates if positions are given by the setpoint_requested event'''
		return self._instance.IsCallbackStreaming

	@property
	def is_tracking(self) -> bool:
		'''Indicates if the robot follows a target given by set_joint_tracking_target() or set_cartesian_tracking_target()'''
		return self._instance.IsTracking

	@property
	def has_active_format(self) -> bool:
		'''Indicates if the format of the positions is fixed. A session uses only one format, chosen by the first queued trajectory, start_tracking() or start_callback_streaming(). While this is true, positions in the other format throw a StreamMotionException with FormatMismatch. It becomes false when the queue is empty and no session is active: call finish() to use the other format in the next session.'''
		return self._instance.HasActiveFormat

	@property
	def active_format(self) -> PositionFormat:
		'''Format of the positions of the current session or of the queued trajectories. Only valid when has_active_format is true.'''
		return PositionFormat(int(self._instance.ActiveFormat))

	@property
	def override(self) -> float:
		'''Speed of the queued trajectories in percent (greater than 0, up to 100, default 100). The robot itself must run at 100% override, so this value slows down the trajectories on their path: the positions are the same, only the time is stretched. A change is applied progressively.'''
		return self._instance.Override

	@override.setter
	def override(self, value: float):
		self._instance.Override = value

	@property
	def is_paused(self) -> bool:
		'''Indicates if the queued trajectories are paused'''
		return self._instance.IsPaused

	@property
	def io_values(self) -> typing.List[IOValue]:
		'''Last values of the ranges of I/O added with add_io_monitor()'''
		__r = self._instance.IOValues
		return None if __r is None else [None if x is None else IOValue(x) for x in __r]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
