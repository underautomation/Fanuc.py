import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SntpCustomVariableType as sntp_custom_variable_type

class SntpCustomVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sntp_custom_variable_type()
		else:
			self._instance = _internal
	@property
	def start_month(self) -> int:
		return self._instance.StartMonth
	@property
	def start_date(self) -> int:
		return self._instance.StartDate
	@property
	def start_hour(self) -> int:
		return self._instance.StartHour
	@property
	def end_month(self) -> int:
		return self._instance.EndMonth
	@property
	def end_date(self) -> int:
		return self._instance.EndDate
	@property
	def end_hour(self) -> int:
		return self._instance.EndHour
	@property
	def local_time(self) -> bool:
		return self._instance.LocalTime
	@property
	def north_hem(self) -> bool:
		return self._instance.NorthHem
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
