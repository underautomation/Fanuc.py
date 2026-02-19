import typing
from UnderAutomation.Fanuc.Rmi.Internal import RmiConnectParametersBase as rmi_connect_parameters_base

class RmiConnectParametersBase:
	'''Base class for RMI connection parameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''RMI bootstrap port number.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def read_timeout_ms(self) -> int:
		'''Read timeout in milliseconds.'''
		return self._instance.ReadTimeoutMs

	@read_timeout_ms.setter
	def read_timeout_ms(self, value: int):
		self._instance.ReadTimeoutMs = value

	@property
	def write_timeout_ms(self) -> int:
		'''Write timeout in milliseconds.'''
		return self._instance.WriteTimeoutMs

	@write_timeout_ms.setter
	def write_timeout_ms(self, value: int):
		self._instance.WriteTimeoutMs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default RMI bootstrap port (16001).
RmiConnectParametersBase.DEFAULT_PORT = rmi_connect_parameters_base.DEFAULT_PORT

# Default read timeout in milliseconds (3000).
RmiConnectParametersBase.DEFAULT_READ_TIMEOUT_MS = rmi_connect_parameters_base.DEFAULT_READ_TIMEOUT_MS

# Default write timeout in milliseconds (3000).
RmiConnectParametersBase.DEFAULT_WRITE_TIMEOUT_MS = rmi_connect_parameters_base.DEFAULT_WRITE_TIMEOUT_MS
