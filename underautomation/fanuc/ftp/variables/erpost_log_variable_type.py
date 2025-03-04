import typing
from underautomation.fanuc.ftp.variables.log_alarm_variable_type import LogAlarmVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ErpostLogVariableType as erpost_log_variable_type

class ErpostLogVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = erpost_log_variable_type()
		else:
			self._instance = _internal
	@property
	def log_enb(self) -> int:
		return self._instance.LogEnb
	@property
	def log_count(self) -> int:
		return self._instance.LogCount
	@property
	def alm_list(self) -> typing.List[LogAlarmVariableType]:
		return [LogAlarmVariableType(x) for x in self._instance.AlmList]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
