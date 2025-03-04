import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SntpCfgVariableType as sntp_cfg_variable_type

class SntpCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sntp_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def server(self) -> str:
		return self._instance.Server
	@property
	def time_win(self) -> int:
		return self._instance.TimeWin
	@property
	def tz_index(self) -> int:
		return self._instance.TzIndex
	@property
	def tz_offset(self) -> int:
		return self._instance.TzOffset
	@property
	def cur_offset(self) -> int:
		return self._instance.CurOffset
	@property
	def dst(self) -> bool:
		return self._instance.Dst
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
