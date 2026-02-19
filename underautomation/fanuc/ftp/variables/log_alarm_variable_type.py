import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import LogAlarmVariableType as log_alarm_variable_type

class LogAlarmVariableType(GenericVariableType):
	'''Describes the Fanuc type LOG_ALARM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_alarm_variable_type()
		else:
			self._instance = _internal

	@property
	def alm_code(self) -> int:
		'''Value of variable $ALM_CODE'''
		return self._instance.AlmCode

	@property
	def alm_number(self) -> int:
		'''Value of variable $ALM_NUMBER'''
		return self._instance.AlmNumber

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogAlarmVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
