import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysTimeVariableType as sys_time_variable_type

class SysTimeVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sys_time_variable_type()
		else:
			self._instance = _internal
	@property
	def minute(self) -> int:
		return self._instance.Minute
	@property
	def hour(self) -> int:
		return self._instance.Hour
	@property
	def day(self) -> int:
		return self._instance.Day
	@property
	def month(self) -> int:
		return self._instance.Month
	@property
	def dow(self) -> int:
		return self._instance.Dow
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
