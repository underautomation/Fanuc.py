import typing
from underautomation.fanuc.telnet.internal.telnet_client_base import TelnetClientBase
from UnderAutomation.Fanuc.Telnet.Internal import TelnetClientInternal as telnet_client_internal

class TelnetClientInternal(TelnetClientBase):
	'''Internal implementation of KCL Client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TelnetClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
