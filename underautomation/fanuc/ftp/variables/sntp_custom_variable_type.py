import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SntpCustomVariableType as sntp_custom_variable_type

class SntpCustomVariableType(GenericVariableType):
	'''Describes the Fanuc type SNTP_CUSTOM_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sntp_custom_variable_type()
		else:
			self._instance = _internal

	@property
	def start_month(self) -> int:
		'''Value of variable $START_MONTH'''
		return self._instance.StartMonth

	@property
	def start_date(self) -> int:
		'''Value of variable $START_DATE'''
		return self._instance.StartDate

	@property
	def start_hour(self) -> int:
		'''Value of variable $START_HOUR'''
		return self._instance.StartHour

	@property
	def end_month(self) -> int:
		'''Value of variable $END_MONTH'''
		return self._instance.EndMonth

	@property
	def end_date(self) -> int:
		'''Value of variable $END_DATE'''
		return self._instance.EndDate

	@property
	def end_hour(self) -> int:
		'''Value of variable $END_HOUR'''
		return self._instance.EndHour

	@property
	def local_time(self) -> bool:
		'''Value of variable $LOCAL_TIME'''
		return self._instance.LocalTime

	@property
	def north_hem(self) -> bool:
		'''Value of variable $NORTH_HEM'''
		return self._instance.NorthHem

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SntpCustomVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
