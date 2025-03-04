import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VarsConfigVariableType as vars_config_variable_type

class VarsConfigVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vars_config_variable_type()
		else:
			self._instance = _internal
	@property
	def shadowrecs(self) -> int:
		return self._instance.Shadowrecs
	@property
	def shad_unscan(self) -> int:
		return self._instance.ShadUnscan
	@property
	def shadowtime(self) -> int:
		return self._instance.Shadowtime
	@property
	def shaddgdet(self) -> int:
		return self._instance.Shaddgdet
	@property
	def legacy(self) -> bool:
		return self._instance.Legacy
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
