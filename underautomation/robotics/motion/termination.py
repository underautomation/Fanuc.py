from __future__ import annotations
import typing
from underautomation.robotics.motion.termination_type import TerminationType
from UnderAutomation.Robotics.Motion import Termination as termination
from UnderAutomation.Robotics.Motion import TerminationType as termination_type

class Termination:
	'''Termination of a motion: stop at the target, overlap with the next motion, or corner region of a given size'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = termination()
		else:
			self._instance = _internal

	@staticmethod
	def stop() -> 'Termination':
		'''The robot stops at the target position'''
		__r = termination.Stop()
		return None if __r is None else Termination(__r)

	@staticmethod
	def overlap(percent: float) -> 'Termination':
		'''The next motion starts during the deceleration of this one

		:param percent: From 0 to 100: part of the deceleration during which both motions are combined. 100 gives the smoothest motion.
		'''
		__r = termination.Overlap(percent)
		return None if __r is None else Termination(__r)

	@staticmethod
	def corner(distance: float) -> 'Termination':
		'''Corner region: the corner is replaced by a smooth curve at constant speed. Only between Cartesian motions.

		:param distance: Distance from the target position where the curve starts and ends, in mm. It is limited to half of the length of each motion.
		'''
		__r = termination.Corner(distance)
		return None if __r is None else Termination(__r)

	@property
	def type(self) -> TerminationType:
		'''Type of termination'''
		return TerminationType(int(self._instance.Type))

	@property
	def value(self) -> float:
		'''Overlap in percent (0 to 100), or corner distance in mm. 0 for a stop.'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Termination):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
