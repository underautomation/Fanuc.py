import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HistEleVariableType as hist_ele_variable_type

class HistEleVariableType(GenericVariableType):
	'''Describes the Fanuc type HIST_ELE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hist_ele_variable_type()
		else:
			self._instance = _internal

	@property
	def time_stamp(self) -> int:
		'''Value of variable $TIME_STAMP'''
		return self._instance.TimeStamp

	@property
	def on_time(self) -> int:
		'''Value of variable $ON_TIME'''
		return self._instance.OnTime

	@property
	def off_time(self) -> int:
		'''Value of variable $OFF_TIME'''
		return self._instance.OffTime

	@property
	def on_percent(self) -> int:
		'''Value of variable $ON_PERCENT'''
		return self._instance.OnPercent

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HistEleVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
