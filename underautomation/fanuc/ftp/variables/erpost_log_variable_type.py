import typing
from underautomation.fanuc.ftp.variables.log_alarm_variable_type import LogAlarmVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ErpostLogVariableType as erpost_log_variable_type

class ErpostLogVariableType(GenericVariableType):
	'''Describes the Fanuc type ERPOST_LOG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = erpost_log_variable_type()
		else:
			self._instance = _internal

	@property
	def log_enb(self) -> int:
		'''Value of variable $LOG_ENB'''
		return self._instance.LogEnb

	@property
	def log_count(self) -> int:
		'''Value of variable $LOG_COUNT'''
		return self._instance.LogCount

	@property
	def alm_list(self) -> typing.List[LogAlarmVariableType]:
		'''Value of variable $ALM_LIST'''
		return [LogAlarmVariableType(x) for x in self._instance.AlmList]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErpostLogVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
