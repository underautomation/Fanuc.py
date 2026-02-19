import typing
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import SetValueResult as set_value_result

class SetValueResult(Result):
	'''Base class for results that contain a former and new value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_value_result()
		else:
			self._instance = _internal

	@property
	def former_value(self) -> str:
		'''Former value before the command'''
		return self._instance.FormerValue

	@property
	def new_value(self) -> str:
		'''New value after the command execution'''
		return self._instance.NewValue

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetValueResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
