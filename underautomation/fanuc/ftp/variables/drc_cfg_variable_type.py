import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DrcCfgVariableType as drc_cfg_variable_type

class DrcCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = drc_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def host1(self) -> str:
		return self._instance.Host1
	@property
	def host2(self) -> str:
		return self._instance.Host2
	@property
	def host3(self) -> str:
		return self._instance.Host3
	@property
	def host4(self) -> str:
		return self._instance.Host4
	@property
	def host5(self) -> str:
		return self._instance.Host5
	@property
	def email_enabl(self) -> bool:
		return self._instance.EmailEnabl
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
