import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HostentVariableType as hostent_variable_type

class HostentVariableType(GenericVariableType):
	'''Describes the Fanuc type HOSTENT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hostent_variable_type()
		else:
			self._instance = _internal

	@property
	def h_name(self) -> str:
		'''Value of variable $H_NAME'''
		return self._instance.HName

	@property
	def h_addrtype(self) -> int:
		'''Value of variable $H_ADDRTYPE'''
		return self._instance.HAddrtype

	@property
	def h_length(self) -> int:
		'''Value of variable $H_LENGTH'''
		return self._instance.HLength

	@property
	def h_addr(self) -> str:
		'''Value of variable $H_ADDR'''
		return self._instance.HAddr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HostentVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
