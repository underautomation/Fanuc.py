from __future__ import annotations
import typing
from UnderAutomation.Robotics.Motion import CartesianLimits as cartesian_limits

class CartesianLimits:
	'''Cartesian velocity, acceleration and jerk limits, for the position (mm) and for the orientation (degrees)'''
	def __init__(self, linearVelocity: float, linearAcceleration: float, linearJerk: float, angularVelocity: float, angularAcceleration: float, angularJerk: float, _internal = 0):
		'''Creates limits with the given values

		:param linearVelocity: Linear velocity limit in mm/s
		:param linearAcceleration: Linear acceleration limit in mm/s²
		:param linearJerk: Linear jerk limit in mm/s³
		:param angularVelocity: Angular velocity limit in deg/s
		:param angularAcceleration: Angular acceleration limit in deg/s²
		:param angularJerk: Angular jerk limit in deg/s³
		'''
		if(_internal == 0):
			self._instance = cartesian_limits(linearVelocity, linearAcceleration, linearJerk, angularVelocity, angularAcceleration, angularJerk)
		else:
			self._instance = _internal

	@property
	def linear_velocity(self) -> float:
		'''Linear velocity limit in mm/s'''
		return self._instance.LinearVelocity

	@linear_velocity.setter
	def linear_velocity(self, value: float):
		self._instance.LinearVelocity = value

	@property
	def linear_acceleration(self) -> float:
		'''Linear acceleration limit in mm/s²'''
		return self._instance.LinearAcceleration

	@linear_acceleration.setter
	def linear_acceleration(self, value: float):
		self._instance.LinearAcceleration = value

	@property
	def linear_jerk(self) -> float:
		'''Linear jerk limit in mm/s³'''
		return self._instance.LinearJerk

	@linear_jerk.setter
	def linear_jerk(self, value: float):
		self._instance.LinearJerk = value

	@property
	def angular_velocity(self) -> float:
		'''Angular velocity limit in deg/s'''
		return self._instance.AngularVelocity

	@angular_velocity.setter
	def angular_velocity(self, value: float):
		self._instance.AngularVelocity = value

	@property
	def angular_acceleration(self) -> float:
		'''Angular acceleration limit in deg/s²'''
		return self._instance.AngularAcceleration

	@angular_acceleration.setter
	def angular_acceleration(self, value: float):
		self._instance.AngularAcceleration = value

	@property
	def angular_jerk(self) -> float:
		'''Angular jerk limit in deg/s³'''
		return self._instance.AngularJerk

	@angular_jerk.setter
	def angular_jerk(self, value: float):
		self._instance.AngularJerk = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianLimits):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
