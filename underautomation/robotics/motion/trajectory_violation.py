from __future__ import annotations
import typing
from underautomation.robotics.motion.limit_type import LimitType
from UnderAutomation.Robotics.Motion import TrajectoryViolation as trajectory_violation
from UnderAutomation.Robotics.Motion import LimitType as limit_type

class TrajectoryViolation:
	'''Limit exceeded by a trajectory at one sample'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trajectory_violation()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''Index of the sample'''
		return self._instance.Index

	@property
	def time(self) -> float:
		'''Time of the sample in seconds'''
		return self._instance.Time

	@property
	def axis(self) -> int:
		'''Axis number (1 to 9). For a Cartesian check: 1 for the position, 2 for the orientation.'''
		return self._instance.Axis

	@property
	def type(self) -> LimitType:
		'''Type of limit exceeded'''
		return LimitType(int(self._instance.Type))

	@property
	def value(self) -> float:
		'''Value reached (absolute value)'''
		return self._instance.Value

	@property
	def limit(self) -> float:
		'''Limit'''
		return self._instance.Limit

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TrajectoryViolation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
