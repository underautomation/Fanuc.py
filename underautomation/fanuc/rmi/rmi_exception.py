import typing
from UnderAutomation.Fanuc.Rmi import RmiException as rmi_exception

class RmiException:
	'''Represents an error reported by the FANUC RMI controller or thrown by the client runtime.'''
	def __init__(self, message: str, inner: typing.Any, _internal = 0):
		'''Constructs a new RmiException with a message and an inner exception.'''
		if(_internal == 0):
			self._instance = rmi_exception(message, inner)
		else:
			self._instance = _internal

	@property
	def error_id(self) -> int:
		'''Gets the controller error id when available (0 means no error id was attached).'''
		return self._instance.ErrorId

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
