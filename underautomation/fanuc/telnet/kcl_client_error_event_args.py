import typing
from UnderAutomation.Fanuc.Telnet import KclClientErrorEventArgs as kcl_client_error_event_args

class KclClientErrorEventArgs:
	'''Event arguments for KCL client error events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kcl_client_error_event_args()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def exception(self) -> typing.Any:
		'''Gets the exception that occurred.'''
		return self._instance.Exception

	@exception.setter
	def exception(self, value: typing.Any):
		self._instance.Exception = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KclClientErrorEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
