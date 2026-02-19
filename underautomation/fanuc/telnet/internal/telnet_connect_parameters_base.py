import typing
from UnderAutomation.Fanuc.Telnet.Internal import TelnetConnectParametersBase as telnet_connect_parameters_base

class TelnetConnectParametersBase:
	'''Base class for Telnet connection parameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_connect_parameters_base()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def telnet_kcl_password(self) -> str:
		'''Gets or sets the Telnet KCL password used for authentication.'''
		return self._instance.TelnetKclPassword

	@telnet_kcl_password.setter
	def telnet_kcl_password(self, value: str):
		self._instance.TelnetKclPassword = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TelnetConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
