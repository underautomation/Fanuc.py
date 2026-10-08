from __future__ import annotations
import typing
from underautomation.robotics.motion.trajectory_violation import TrajectoryViolation
from UnderAutomation.Robotics.Motion import CartesianTrajectoryReport as cartesian_trajectory_report

class CartesianTrajectoryReport:
	'''Result of the check of a Cartesian trajectory against Cartesian velocity, acceleration and jerk limits'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_trajectory_report()
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
	def max_linear_velocity(self) -> float:
		'''Highest linear velocity in mm/s'''
		return self._instance.MaxLinearVelocity

	@property
	def max_linear_acceleration(self) -> float:
		'''Highest linear acceleration in mm/s²'''
		return self._instance.MaxLinearAcceleration

	@property
	def max_linear_jerk(self) -> float:
		'''Highest linear jerk in mm/s³'''
		return self._instance.MaxLinearJerk

	@property
	def max_angular_velocity(self) -> float:
		'''Highest angular velocity in deg/s'''
		return self._instance.MaxAngularVelocity

	@property
	def max_angular_acceleration(self) -> float:
		'''Highest angular acceleration in deg/s²'''
		return self._instance.MaxAngularAcceleration

	@property
	def max_angular_jerk(self) -> float:
		'''Highest angular jerk in deg/s³'''
		return self._instance.MaxAngularJerk

	@property
	def violation_count(self) -> int:
		'''Total number of values that exceed a limit'''
		return self._instance.ViolationCount

	@property
	def violations(self) -> typing.List[TrajectoryViolation]:
		'''First violations (at most 100). Axis 1 is the position, axis 2 the orientation.'''
		__r = self._instance.Violations
		return None if __r is None else [None if x is None else TrajectoryViolation(x) for x in __r]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianTrajectoryReport):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
