from __future__ import annotations
import typing
from underautomation.robotics.motion.trajectory_violation import TrajectoryViolation
from UnderAutomation.Robotics.Motion import TrajectoryReport as trajectory_report

class TrajectoryReport:
	'''Result of the check of a joint trajectory against velocity, acceleration and jerk limits'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trajectory_report()
		else:
			self._instance = _internal

	@property
	def is_valid(self) -> bool:
		'''True when no limit is exceeded'''
		return self._instance.IsValid

	@property
	def sample_count(self) -> int:
		'''Number of samples checked'''
		return self._instance.SampleCount

	@property
	def cycle_time(self) -> float:
		'''Period used for the check, in seconds'''
		return self._instance.CycleTime

	@property
	def max_velocity(self) -> typing.List[float]:
		'''Highest velocity of each axis (9 values)'''
		return self._instance.MaxVelocity

	@property
	def max_acceleration(self) -> typing.List[float]:
		'''Highest acceleration of each axis (9 values)'''
		return self._instance.MaxAcceleration

	@property
	def max_jerk(self) -> typing.List[float]:
		'''Highest jerk of each axis (9 values)'''
		return self._instance.MaxJerk

	@property
	def violation_count(self) -> int:
		'''Total number of values that exceed a limit'''
		return self._instance.ViolationCount

	@property
	def violations(self) -> typing.List[TrajectoryViolation]:
		'''First violations (at most 100)'''
		__r = self._instance.Violations
		return None if __r is None else [None if x is None else TrajectoryViolation(x) for x in __r]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TrajectoryReport):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
