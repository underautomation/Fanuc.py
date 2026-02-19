import typing
from underautomation.fanuc.telnet.set_value_result import SetValueResult
from UnderAutomation.Fanuc.Telnet import SetPortResult as set_port_result

class SetPortResult(SetValueResult):
	'''Result of a set port command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_port_result()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetPortResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
