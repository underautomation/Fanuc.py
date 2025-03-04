import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import KarelCfgVariableType as karel_cfg_variable_type

class KarelCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = karel_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def conv_enable(self) -> bool:
		return self._instance.ConvEnable
	@property
	def conv_ctrl(self) -> bool:
		return self._instance.ConvCtrl
	@property
	def conv_flags(self) -> int:
		return self._instance.ConvFlags
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
