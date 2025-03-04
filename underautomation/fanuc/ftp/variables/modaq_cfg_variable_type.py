import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ModaqCfgVariableType as modaq_cfg_variable_type

class ModaqCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = modaq_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def on_line(self) -> bool:
		return self._instance.OnLine
	@property
	def mf_flag(self) -> int:
		return self._instance.MfFlag
	@property
	def mi_flag(self) -> int:
		return self._instance.MiFlag
	@property
	def grp_num(self) -> int:
		return self._instance.GrpNum
	@property
	def startlog(self) -> int:
		return self._instance.Startlog
	@property
	def endlog(self) -> int:
		return self._instance.Endlog
	@property
	def ln_mask(self) -> int:
		return self._instance.LnMask
	@property
	def support(self) -> int:
		return self._instance.Support
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
