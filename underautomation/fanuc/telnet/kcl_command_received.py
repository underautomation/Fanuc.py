import typing
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import KclCommandReceived as kcl_command_received

class KclCommandReceived:
	'''Event arguments for KCL command received events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kcl_command_received()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def result(self) -> Result:
		'''Gets the result of the received command.'''
		return Result(self._instance.Result)

	@result.setter
	def result(self, value: Result):
		self._instance.Result = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KclCommandReceived):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
