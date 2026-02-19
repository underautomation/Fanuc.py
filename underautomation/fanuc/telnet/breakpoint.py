import typing
from UnderAutomation.Fanuc.Telnet import Breakpoint as breakpoint

class Breakpoint:
	'''Represents a breakpoint set on a task line.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = breakpoint()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def line(self) -> int:
		'''Gets the line number where the breakpoint is set.'''
		return self._instance.Line

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Breakpoint):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
