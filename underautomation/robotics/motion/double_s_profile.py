from __future__ import annotations
import typing
from UnderAutomation.Robotics.Motion import DoubleSProfile as double_s_profile

class DoubleSProfile:
	'''One-dimensional motion profile with bounded velocity, acceleration and jerk (7 phases, "double S" profile). The acceleration is zero at the start and at the end. Start and end velocities can be different from zero.'''
	def __init__(self, startPosition: float, endPosition: float, startVelocity: float, endVelocity: float, maxVelocity: float, maxAcceleration: float, maxJerk: float, _internal = 0):
		'''Computes the fastest profile from a start position to an end position with the given limits

		:param startPosition: Start position
		:param endPosition: End position
		:param startVelocity: Velocity at the start
		:param endVelocity: Velocity at the end
		:param maxVelocity: Velocity limit (greater than 0)
		:param maxAcceleration: Acceleration limit (greater than 0)
		:param maxJerk: Jerk limit (greater than 0)
		'''
		if(_internal == 0):
			self._instance = double_s_profile(startPosition, endPosition, startVelocity, endVelocity, maxVelocity, maxAcceleration, maxJerk)
		else:
			self._instance = _internal

	def get_position(self, time: float) -> float:
		'''Position at the given time (limited to [0, duration])

		:param time: Time in seconds
		'''
		return self._instance.GetPosition(time)

	def get_velocity(self, time: float) -> float:
		'''Velocity at the given time (limited to [0, duration])

		:param time: Time in seconds
		'''
		return self._instance.GetVelocity(time)

	def get_acceleration(self, time: float) -> float:
		'''Acceleration at the given time (limited to [0, duration])

		:param time: Time in seconds
		'''
		return self._instance.GetAcceleration(time)

	def get_jerk(self, time: float) -> float:
		'''Jerk at the given time (limited to [0, duration])

		:param time: Time in seconds
		'''
		return self._instance.GetJerk(time)

	def stretch_to(self, duration: float) -> 'DoubleSProfile':
		'''Returns the same motion slowed down to last the given duration. The velocity is divided by k, the acceleration by k² and the jerk by k³, where k is the ratio of the durations, so the limits are still respected. Only for profiles that start and end at rest.

		:param duration: New duration in seconds, not lower than duration
		'''
		return DoubleSProfile(None, None, None, None, None, None, None, self._instance.StretchTo(duration))

	@property
	def start_position(self) -> float:
		'''Start position'''
		return self._instance.StartPosition

	@property
	def end_position(self) -> float:
		'''End position'''
		return self._instance.EndPosition

	@property
	def start_velocity(self) -> float:
		'''Velocity at the start'''
		return self._instance.StartVelocity

	@property
	def end_velocity(self) -> float:
		'''Velocity at the end'''
		return self._instance.EndVelocity

	@property
	def max_velocity(self) -> float:
		'''Velocity limit used to compute the profile'''
		return self._instance.MaxVelocity

	@property
	def max_acceleration(self) -> float:
		'''Acceleration limit used to compute the profile'''
		return self._instance.MaxAcceleration

	@property
	def max_jerk(self) -> float:
		'''Jerk limit used to compute the profile'''
		return self._instance.MaxJerk

	@property
	def duration(self) -> float:
		'''Duration of the profile in seconds'''
		return self._instance.Duration

	@property
	def acceleration_time(self) -> float:
		'''Duration of the acceleration phase in seconds'''
		return self._instance.AccelerationTime

	@property
	def constant_velocity_time(self) -> float:
		'''Duration of the constant velocity phase in seconds'''
		return self._instance.ConstantVelocityTime

	@property
	def deceleration_time(self) -> float:
		'''Duration of the deceleration phase in seconds'''
		return self._instance.DecelerationTime

	@property
	def peak_velocity(self) -> float:
		'''Highest velocity reached (absolute value)'''
		return self._instance.PeakVelocity

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DoubleSProfile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
