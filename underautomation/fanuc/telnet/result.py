import typing
from UnderAutomation.Fanuc.Telnet import Result as result

class Result:
	'''Abstract base class for all KCL command results.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = result()
		else:
			self._instance = _internal

	@property
	def error_text(self) -> str:
		'''Error text if any error occured during command execution'''
		return self._instance.ErrorText

	@property
	def succeed(self) -> bool:
		'''Command succeeded if no error text is present'''
		return self._instance.Succeed

	@property
	def kcl_command(self) -> str:
		'''The KCL command that was sent to the controller'''
		return self._instance.KclCommand

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Result):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
