import typing
from underautomation.fanuc.telnet.base_result import BaseResult
from UnderAutomation.Fanuc.Telnet import UnsimulateResult as unsimulate_result

class UnsimulateResult(BaseResult):
	'''Result of an unsimulate port command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = unsimulate_result()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UnsimulateResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
