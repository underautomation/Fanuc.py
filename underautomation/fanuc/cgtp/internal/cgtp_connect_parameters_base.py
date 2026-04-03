from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp.Internal import CgtpConnectParametersBase as cgtp_connect_parameters_base

class CgtpConnectParametersBase:
	'''Base class for CGTP Web Server connection parameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''HTTP port number of the CGTP Web Server.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def request_timeout_ms(self) -> int:
		'''HTTP request timeout in milliseconds.'''
		return self._instance.RequestTimeoutMs

	@request_timeout_ms.setter
	def request_timeout_ms(self, value: int):
		self._instance.RequestTimeoutMs = value

	@property
	def login(self) -> str:
		'''Login for HTTP Basic authentication (optional).'''
		return self._instance.Login

	@login.setter
	def login(self, value: str):
		self._instance.Login = value

	@property
	def password(self) -> str:
		'''Password for HTTP Basic authentication (optional).'''
		return self._instance.Password

	@password.setter
	def password(self, value: str):
		self._instance.Password = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default HTTP port for CGTP Web Server.
CgtpConnectParametersBase.DEFAULT_PORT = cgtp_connect_parameters_base.DEFAULT_PORT

# Default request timeout in milliseconds.
CgtpConnectParametersBase.DEFAULT_REQUEST_TIMEOUT_MS = cgtp_connect_parameters_base.DEFAULT_REQUEST_TIMEOUT_MS
