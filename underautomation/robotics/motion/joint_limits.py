from __future__ import annotations
import typing
from UnderAutomation.Robotics.Motion import JointLimits as joint_limits

class JointLimits:
	'''Velocity, acceleration and jerk limits of the 9 axes of a robot. Units are degrees (mm for linear axes) per second, per second squared and per second cubed. A limit of 0 means that the axis is not present or not limited.'''
	def __init__(self, velocity: typing.List[float], acceleration: typing.List[float], jerk: typing.List[float], _internal = 0):
		'''Creates limits from arrays of values. Arrays can contain less than 9 values, missing values are set to 0.

		:param velocity: Velocity limit of each axis
		:param acceleration: Acceleration limit of each axis
		:param jerk: Jerk limit of each axis
		'''
		if(_internal == 0):
			self._instance = joint_limits(velocity, acceleration, jerk)
		else:
			self._instance = _internal

	def scale(self, velocityFactor: float, accelerationFactor: float, jerkFactor: float) -> 'JointLimits':
		'''Returns a copy of these limits where each value is multiplied by the given factors

		:param velocityFactor: Factor applied to velocity limits
		:param accelerationFactor: Factor applied to acceleration limits
		:param jerkFactor: Factor applied to jerk limits
		'''
		return JointLimits(None, None, None, self._instance.Scale(velocityFactor, accelerationFactor, jerkFactor))

	@property
	def velocity(self) -> typing.List[float]:
		'''Velocity limit of each axis (9 values)'''
		return self._instance.Velocity

	@property
	def acceleration(self) -> typing.List[float]:
		'''Acceleration limit of each axis (9 values)'''
		return self._instance.Acceleration

	@property
	def jerk(self) -> typing.List[float]:
		'''Jerk limit of each axis (9 values)'''
		return self._instance.Jerk

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointLimits):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Number of axes handled by this class
JointLimits.AxisCount = joint_limits.AxisCount
