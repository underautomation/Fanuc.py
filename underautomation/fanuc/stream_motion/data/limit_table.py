from __future__ import annotations
import typing
from underautomation.robotics.motion.limit_type import LimitType
from UnderAutomation.Fanuc.StreamMotion.Data import LimitTable as limit_table
from UnderAutomation.Robotics.Motion import LimitType as limit_type

class LimitTable:
	'''Table of allowable limits of one axis for one type of limit. The limit depends on the speed of the flange center: the table gives 20 values, for speeds up to 1/20, 2/20, ... 20/20 of max_speed, with no payload and with the maximum payload.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = limit_table()
		else:
			self._instance = _internal

	def get_value(self, flangeSpeed: float, payload: float, maxPayload: float) -> float:
		'''Computes the limit for a given flange speed and payload, as the robot does when $STMO_GRP[1].$LMT_MODE is 0: linear interpolation between the speed stages (the first stage applies below Vmax/20, and values are extrapolated above Vmax), then linear interpolation between no payload and maximum payload.

		:param flangeSpeed: Peak speed of the flange center, in mm/s
		:param payload: Payload mass, in kg
		:param maxPayload: Maximum payload of the robot, in kg
		'''
		return self._instance.GetValue(flangeSpeed, payload, maxPayload)

	@property
	def axis(self) -> int:
		'''Axis number (1 to 9)'''
		return self._instance.Axis

	@property
	def type(self) -> LimitType:
		'''Type of limit'''
		return LimitType(int(self._instance.Type))

	@property
	def max_speed(self) -> float:
		'''Maximum speed of the flange center (Vmax, system variable $STMO_GRP[1].$MAX_SPD), in mm/s'''
		return self._instance.MaxSpeed

	@property
	def intermediate_check_time(self) -> float:
		'''Time interval of the intermediate check of the limits, in seconds'''
		return self._instance.IntermediateCheckTime

	@property
	def no_payload(self) -> typing.List[float]:
		'''Limits with no payload, for flange speeds up to 1/20, 2/20, ... 20/20 of max_speed (20 values)'''
		return self._instance.NoPayload

	@property
	def max_payload(self) -> typing.List[float]:
		'''Limits with the maximum payload, for flange speeds up to 1/20, 2/20, ... 20/20 of max_speed (20 values)'''
		return self._instance.MaxPayload

	@property
	def reference_value(self) -> float:
		'''Reference limit: value with the maximum payload at the maximum speed. It is the value of the system variables $STMO_GRP[1].$JNT_VEL_LIM, $JNT_ACC_LIM or $JNT_JRK_LIM.'''
		return self._instance.ReferenceValue

	@property
	def is_axis_present(self) -> bool:
		'''Indicates if the axis exists (at least one value is not 0)'''
		return self._instance.IsAxisPresent

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LimitTable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Number of speed stages of a table
LimitTable.StageCount = limit_table.StageCount
