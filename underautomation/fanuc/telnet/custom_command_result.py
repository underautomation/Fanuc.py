import typing
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import CustomCommandResult as custom_command_result

class CustomCommandResult(Result):
	'''Result of a custom KCL command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = custom_command_result()
		else:
			self._instance = _internal

	@property
	def data(self) -> str:
		'''Gets the raw data returned by the custom command.'''
		return self._instance.Data

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CustomCommandResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
