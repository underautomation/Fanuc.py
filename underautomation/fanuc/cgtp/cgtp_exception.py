import typing
from __future__ import annotation
from UnderAutomation.Fanuc.Cgtp import CgtpException as cgtp_exception

class CgtpException:
	'''Represents an error returned by the FANUC COMET RPC interface.'''
	def __init__(self, message: str, inner: typing.Any, _internal = 0):
		'''Constructs a new CgtpException with a message and inner exception.'''
		if(_internal == 0):
			self._instance = cgtp_exception(message, inner)
		else:
			self._instance = _internal

	@property
	def status(self) -> int:
		'''The RPC status code returned by the controller when available.'''
		return self._instance.Status

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
