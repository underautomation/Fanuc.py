import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HistEleVariableType as hist_ele_variable_type

class HistEleVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hist_ele_variable_type()
		else:
			self._instance = _internal
	@property
	def time_stamp(self) -> int:
		return self._instance.TimeStamp
	@property
	def on_time(self) -> int:
		return self._instance.OnTime
	@property
	def off_time(self) -> int:
		return self._instance.OffTime
	@property
	def on_percent(self) -> int:
		return self._instance.OnPercent
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
