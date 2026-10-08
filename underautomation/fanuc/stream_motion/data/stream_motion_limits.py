from __future__ import annotations
import typing
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.fanuc.stream_motion.data.limit_table import LimitTable
from underautomation.robotics.motion.limit_type import LimitType
from UnderAutomation.Fanuc.StreamMotion.Data import StreamMotionLimits as stream_motion_limits
from UnderAutomation.Robotics.Motion import LimitType as limit_type

class StreamMotionLimits:
	'''Allowable velocity, acceleration and jerk limits of the robot axes, read from the robot. The robot stops with an alarm when a position sent to it exceeds these limits.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_limits()
		else:
			self._instance = _internal

	def get_table(self, axis: int, type: LimitType) -> LimitTable:
		'''Returns the table of limits of one axis

		:param axis: Axis number (1 to 9)
		:param type: Type of limit
		'''
		__r = self._instance.GetTable(axis, limit_type(int(type)))
		return None if __r is None else LimitTable(__r)

	def compute_limits(self, flangeSpeed: float, payload: float, maxPayload: float) -> JointLimits:
		'''Computes the limits of all axes for a given flange speed and payload, as the robot does when $STMO_GRP[1].$LMT_MODE is 0.

		:param flangeSpeed: Peak speed of the flange center, in mm/s
		:param payload: Payload mass, in kg
		:param maxPayload: Maximum payload of the robot, in kg
		'''
		__r = self._instance.ComputeLimits(flangeSpeed, payload, maxPayload)
		return None if __r is None else JointLimits(None, None, None, __r)

	@property
	def axis_count(self) -> int:
		'''Number of axes of the robot (axes with limits)'''
		return self._instance.AxisCount

	@property
	def max_speed(self) -> float:
		'''Maximum speed of the flange center (Vmax, system variable $STMO_GRP[1].$MAX_SPD), in mm/s'''
		return self._instance.MaxSpeed

	@property
	def intermediate_check_time(self) -> float:
		'''Time interval of the intermediate check of the limits, in seconds'''
		return self._instance.IntermediateCheckTime

	@property
	def reference_limits(self) -> JointLimits:
		'''Reference limits of each axis: values with the maximum payload at the maximum speed. They are equal to the system variables $STMO_GRP[1].$JNT_VEL_LIM, $JNT_ACC_LIM and $JNT_JRK_LIM, and they are always safe.'''
		__r = self._instance.ReferenceLimits
		return None if __r is None else JointLimits(None, None, None, __r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionLimits):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
