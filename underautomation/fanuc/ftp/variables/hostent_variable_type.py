import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HostentVariableType as hostent_variable_type

class HostentVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hostent_variable_type()
		else:
			self._instance = _internal
	@property
	def h_name(self) -> str:
		return self._instance.HName
	@property
	def h_addrtype(self) -> int:
		return self._instance.HAddrtype
	@property
	def h_length(self) -> int:
		return self._instance.HLength
	@property
	def h_addr(self) -> str:
		return self._instance.HAddr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
