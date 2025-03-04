import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DmswCfgVariableType as dmsw_cfg_variable_type

class DmswCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dmsw_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def keyimage(self) -> int:
		return self._instance.Keyimage
	@property
	def tms_dsb(self) -> bool:
		return self._instance.TmsDsb
	@property
	def tms_stat(self) -> int:
		return self._instance.TmsStat
	@property
	def tms_input(self) -> int:
		return self._instance.TmsInput
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
