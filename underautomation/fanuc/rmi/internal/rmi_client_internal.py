import typing
from underautomation.fanuc.rmi.internal.rmi_client_base import RmiClientBase
from UnderAutomation.Fanuc.Rmi.Internal import RmiClientInternal as rmi_client_internal

class RmiClientInternal(RmiClientBase):
	'''Internal RMI client used by the library infrastructure.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
