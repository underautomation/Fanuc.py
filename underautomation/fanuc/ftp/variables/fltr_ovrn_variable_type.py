import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FltrOvrnVariableType as fltr_ovrn_variable_type

class FltrOvrnVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fltr_ovrn_variable_type()
		else:
			self._instance = _internal
	@property
	def limit_tick(self) -> int:
		return self._instance.LimitTick
	@property
	def overrun_cnt(self) -> int:
		return self._instance.OverrunCnt
	@property
	def max_tick(self) -> int:
		return self._instance.MaxTick
	@property
	def itp_count(self) -> int:
		return self._instance.ItpCount
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
