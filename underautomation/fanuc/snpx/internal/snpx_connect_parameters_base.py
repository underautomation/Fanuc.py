import typing
from UnderAutomation.Fanuc.Snpx.Internal import SnpxConnectParametersBase as snpx_connect_parameters_base

class SnpxConnectParametersBase:
	'''Base class for SNPX connection parameters.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_connect_parameters_base()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def port(self) -> int:
		'''Gets or sets the port number for the SNPX connection.'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# The default SNPX port number.
SnpxConnectParametersBase.DEFAULT_PORT = snpx_connect_parameters_base.DEFAULT_PORT
