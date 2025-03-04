import typing
from underautomation.fanuc.ftp.variables.condet_data_variable_type import CondetDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CondetCfgVariableType as condet_cfg_variable_type

class CondetCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def state(self) -> int:
		return self._instance.State
	@property
	def server_name(self) -> str:
		return self._instance.ServerName
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def protocol(self) -> int:
		return self._instance.Protocol
	@property
	def peer_name(self) -> str:
		return self._instance.PeerName
	@property
	def ext_mask(self) -> int:
		return self._instance.ExtMask
	@property
	def ext_used(self) -> int:
		return self._instance.ExtUsed
	@property
	def ext_data(self) -> typing.List[CondetDataVariableType]:
		return [CondetDataVariableType(x) for x in self._instance.ExtData]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
