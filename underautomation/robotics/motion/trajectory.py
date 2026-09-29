from __future__ import annotations
import typing
from underautomation.robotics.motion.position_format import PositionFormat
from underautomation.robotics.motion.io_event import IOEvent
from underautomation.robotics.io.digital_signal import DigitalSignal
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.geometry.cartesian_pose import CartesianPose
from underautomation.robotics.motion.trajectory_report import TrajectoryReport
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.cartesian_trajectory_report import CartesianTrajectoryReport
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from UnderAutomation.Robotics.Motion import Trajectory as trajectory
from UnderAutomation.Robotics.Motion import PositionFormat as position_format

class Trajectory:
	'''Robot trajectory in joint or Cartesian format. A trajectory can be evaluated at any time between 0 and duration, and can carry I/O events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trajectory()
		else:
			self._instance = _internal

	def add_io_event(self, time: float, signal: DigitalSignal, value: bool) -> None:
		'''Adds a digital signal change at a given time of the trajectory

		:param time: Time from the start of the trajectory, in seconds (between 0 and duration)
		:param signal: Signal to write
		:param value: Value to write
		'''
		self._instance.AddIOEvent(time, signal._instance if signal else None, value)

	def get_joints(self, time: float) -> JointValues:
		'''Returns the joint position at the given time. The trajectory must be in joint format.

		:param time: Time from the start of the trajectory, in seconds. It is limited to the range [0, duration].
		'''
		return JointValues(None, self._instance.GetJoints(time))

	def get_cartesian(self, time: float) -> CartesianPose:
		'''Returns the Cartesian pose at the given time. The trajectory must be in Cartesian format.

		:param time: Time from the start of the trajectory, in seconds. It is limited to the range [0, duration].
		'''
		return CartesianPose(None, None, None, None, self._instance.GetCartesian(time))

	def sample_joints(self, cycleTime: float) -> typing.List[JointValues]:
		'''Samples the trajectory at a fixed period. The trajectory must be in joint format.

		:param cycleTime: Period between two samples, in seconds
		:returns: Positions from time 0 to the end of the trajectory
		'''
		return [JointValues(None, x) for x in self._instance.SampleJoints(cycleTime)]

	def sample_cartesian(self, cycleTime: float) -> typing.List[CartesianPose]:
		'''Samples the trajectory at a fixed period. The trajectory must be in Cartesian format.

		:param cycleTime: Period between two samples, in seconds
		:returns: Poses from time 0 to the end of the trajectory
		'''
		return [CartesianPose(None, None, None, None, x) for x in self._instance.SampleCartesian(cycleTime)]

	@staticmethod
	def from_joint_samples(samples: typing.List[JointValues], cycleTime: float) -> 'Trajectory':
		'''Creates a joint trajectory from positions taken at a fixed period. When the trajectory is streamed to a robot at the same period, the positions are sent without any change.

		:param samples: Joint positions, one per period (up to MaxJointCount axes)
		:param cycleTime: Period between two positions, in seconds
		'''
		return Trajectory(trajectory.FromJointSamples([x._instance if x else None for x in samples], cycleTime))

	@staticmethod
	def from_cartesian_samples(samples: typing.List[CartesianPose], cycleTime: float) -> 'Trajectory':
		'''Creates a Cartesian trajectory from poses taken at a fixed period. When the trajectory is streamed to a robot at the same period, the poses are sent without any change.

		:param samples: Cartesian poses, one per period (up to MaxExternalAxisCount external axes)
		:param cycleTime: Period between two poses, in seconds
		'''
		return Trajectory(trajectory.FromCartesianSamples([x._instance if x else None for x in samples], cycleTime))

	@staticmethod
	def from_timed_joints(points: typing.List[JointValues], times: typing.List[float]) -> 'Trajectory':
		'''Creates a joint trajectory that passes through positions at given times. The positions are joined by a smooth curve (cubic spline), and the robot is at rest at the first and the last position. The times are kept: use check() to verify the limits, and retime() to slow down the trajectory if needed.

		:param points: Joint positions (at least 2)
		:param times: Time of each position in seconds, strictly increasing. The trajectory starts at the first time.
		'''
		return Trajectory(trajectory.FromTimedJoints([x._instance if x else None for x in points], times))

	@staticmethod
	def from_timed_cartesian(points: typing.List[CartesianPose], times: typing.List[float]) -> 'Trajectory':
		'''Creates a Cartesian trajectory that passes through poses at given times. The poses are joined by a smooth curve (cubic spline), and the robot is at rest at the first and the last pose. The orientation is interpolated with quaternions, so it has no singularity. The times are kept: use check_cartesian() to verify the limits, and retime_cartesian() to slow down the trajectory if needed.

		:param points: Cartesian poses, at least 2
		:param times: Time of each pose in seconds, strictly increasing. The trajectory starts at the first time.
		'''
		return Trajectory(trajectory.FromTimedCartesian([x._instance if x else None for x in points], times))

	def check(self, limits: JointLimits, cycleTime: float, singlePrecision: bool) -> TrajectoryReport:
		'''Checks the velocity, acceleration and jerk of each axis as a robot computes them from a stream of positions: positions sampled at the communication cycle, differences between consecutive positions divided by the cycle time, and positions before the first one equal to the first one. The trajectory must be in joint format.

		:param limits: Limits of each axis. Axes with a limit of 0 are not checked.
		:param cycleTime: Communication cycle of the robot in seconds
		:param singlePrecision: True to round the positions to single precision first, when the robot receives them in single precision
		'''
		return TrajectoryReport(self._instance.Check(limits._instance if limits else None, cycleTime, singlePrecision))

	def check_cartesian(self, limits: CartesianLimits, cycleTime: float) -> CartesianTrajectoryReport:
		'''Checks the linear and angular velocity, acceleration and jerk, computed from positions sampled at the communication cycle. The trajectory must be in Cartesian format. The joint limits of the robot cannot be checked from Cartesian positions.

		:param limits: Cartesian limits. Values of 0 are not checked.
		:param cycleTime: Communication cycle of the robot in seconds
		'''
		return CartesianTrajectoryReport(self._instance.CheckCartesian(limits._instance if limits else None, cycleTime))

	def retime(self, limits: JointLimits, cycleTime: float, singlePrecision: bool=False) -> 'Trajectory':
		'''Returns the same path played slower so that the joint limits are respected (see check()). The positions are the same, only the time is stretched. Returns this trajectory when it is already valid.

		:param limits: Limits of each axis
		:param cycleTime: Communication cycle of the robot in seconds
		:param singlePrecision: True to check the positions rounded to single precision, when the robot receives them in single precision
		'''
		return Trajectory(self._instance.Retime(limits._instance if limits else None, cycleTime, singlePrecision))

	def retime_cartesian(self, limits: CartesianLimits, cycleTime: float) -> 'Trajectory':
		'''Returns the same path played slower so that the Cartesian limits are respected (see check_cartesian()). The positions are the same, only the time is stretched. Returns this trajectory when it is already valid.

		:param limits: Cartesian limits
		:param cycleTime: Communication cycle of the robot in seconds
		'''
		return Trajectory(self._instance.RetimeCartesian(limits._instance if limits else None, cycleTime))

	@property
	def format(self) -> PositionFormat:
		'''Format of the positions of this trajectory'''
		return PositionFormat(int(self._instance.Format))

	@property
	def duration(self) -> float:
		'''Duration of the trajectory in seconds'''
		return self._instance.Duration

	@property
	def cycle_time(self) -> float:
		'''Period between two samples in seconds, when the trajectory was created from samples. 0 otherwise.'''
		return self._instance.CycleTime

	@property
	def starts_at_rest(self) -> bool:
		'''Indicates if the velocity and the acceleration are zero at the start of the trajectory'''
		return self._instance.StartsAtRest

	@property
	def ends_at_rest(self) -> bool:
		'''Indicates if the velocity and the acceleration are zero at the end of the trajectory'''
		return self._instance.EndsAtRest

	@property
	def io_events(self) -> typing.List[IOEvent]:
		'''I/O events of this trajectory, sorted by time'''
		return [IOEvent(None, None, None, x) for x in self._instance.IOEvents]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Trajectory):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Maximum number of axes of a joint trajectory
Trajectory.MaxJointCount = trajectory.MaxJointCount

# Maximum number of external axes of a Cartesian trajectory
Trajectory.MaxExternalAxisCount = trajectory.MaxExternalAxisCount
