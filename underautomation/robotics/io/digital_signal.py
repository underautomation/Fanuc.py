from __future__ import annotations
import typing
from UnderAutomation.Robotics.IO import DigitalSignal as digital_signal

class DigitalSignal:
	'''Digital signal of a robot controller, identified by a group and an index. The names of the groups and the valid indexes depend on the robot.'''
	def __init__(self, group: str, index: int, _internal = 0):
		'''Creates a digital signal

		:param group: Group of the signal, as defined by the robot
		:param index: Index of the signal in its group
		'''
		if(_internal == 0):
			self._instance = digital_signal(group, index)
		else:
			self._instance = _internal

	@property
	def group(self) -> str:
		'''Group of the signal, as defined by the robot'''
		return self._instance.Group

	@property
	def index(self) -> int:
		'''Index of the signal in its group'''
		return self._instance.Index

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DigitalSignal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
