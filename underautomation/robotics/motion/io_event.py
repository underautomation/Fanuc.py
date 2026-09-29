from __future__ import annotations
import typing
from underautomation.robotics.io.digital_signal import DigitalSignal
from UnderAutomation.Robotics.Motion import IOEvent as io_event

class IOEvent:
	'''Digital signal change requested at a given time of a trajectory'''
	def __init__(self, time: float, signal: DigitalSignal, value: bool, _internal = 0):
		'''Creates an I/O event

		:param time: Time from the start of the trajectory, in seconds
		:param signal: Signal to write
		:param value: Value to write
		'''
		if(_internal == 0):
			self._instance = io_event(time, signal._instance if signal else None, value)
		else:
			self._instance = _internal

	@property
	def time(self) -> float:
		'''Time from the start of the trajectory, in seconds'''
		return self._instance.Time

	@property
	def signal(self) -> DigitalSignal:
		'''Signal to write'''
		return DigitalSignal(None, None, self._instance.Signal)

	@property
	def value(self) -> bool:
		'''Value to write'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOEvent):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
