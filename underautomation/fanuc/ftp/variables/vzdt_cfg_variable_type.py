import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VzdtCfgVariableType as vzdt_cfg_variable_type

class VzdtCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vzdt_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def allow_image(self) -> bool:
		return self._instance.AllowImage
	@property
	def period(self) -> int:
		return self._instance.Period
	@property
	def msg_qsiz(self) -> int:
		return self._instance.MsgQsiz
	@property
	def size_lim(self) -> int:
		return self._instance.SizeLim
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
