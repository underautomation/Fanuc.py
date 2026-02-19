import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SysTimeVariableType as sys_time_variable_type

class SysTimeVariableType(GenericVariableType):
	'''Describes the Fanuc type SYS_TIME_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sys_time_variable_type()
		else:
			self._instance = _internal

	@property
	def minute(self) -> int:
		'''Value of variable $MINUTE'''
		return self._instance.Minute

	@property
	def hour(self) -> int:
		'''Value of variable $HOUR'''
		return self._instance.Hour

	@property
	def day(self) -> int:
		'''Value of variable $DAY'''
		return self._instance.Day

	@property
	def month(self) -> int:
		'''Value of variable $MONTH'''
		return self._instance.Month

	@property
	def dow(self) -> int:
		'''Value of variable $DOW'''
		return self._instance.Dow

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysTimeVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
