import typing
from underautomation.fanuc.rmi.internal.rmi_client_base import RmiClientBase
from UnderAutomation.Fanuc.Rmi import RmiClient as rmi_client

class RmiClient(RmiClientBase):
	'''RMI client for connecting to and controlling FANUC robots via the Remote Motion Interface protocol.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the RMI client.'''
		if(_internal == 0):
			self._instance = rmi_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: int=16001, readTimeoutMs: int=3000, writeTimeoutMs: int=3000) -> None:
		'''Connect to the FANUC controller using the RMI protocol.

		:param ip: Controller IP address or hostname.
		:param port: Bootstrap port number.
		:param readTimeoutMs: Read timeout in milliseconds.
		:param writeTimeoutMs: Write timeout in milliseconds.
		'''
		self._instance.Connect(ip, port, readTimeoutMs, writeTimeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
