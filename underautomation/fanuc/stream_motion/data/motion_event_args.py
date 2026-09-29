from __future__ import annotations
import typing
from UnderAutomation.Fanuc.StreamMotion.Data import MotionEventArgs as motion_event_args

class MotionEventArgs:
	'''Arguments of the motion events'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_event_args()
		else:
			self._instance = _internal

	@property
	def motion_id(self) -> int:
		'''Identifier of the motion, returned by Enqueue. 0 if there is no motion.'''
		return self._instance.MotionId

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
