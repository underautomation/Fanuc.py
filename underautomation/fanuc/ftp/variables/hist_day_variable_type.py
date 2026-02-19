import typing
from underautomation.fanuc.ftp.variables.hist_ele_variable_type import HistEleVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HistDayVariableType as hist_day_variable_type

class HistDayVariableType(GenericVariableType):
	'''Describes the Fanuc type HIST_DAY_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hist_day_variable_type()
		else:
			self._instance = _internal

	@property
	def date(self) -> int:
		'''Value of variable $DATE'''
		return self._instance.Date

	@property
	def date_str(self) -> str:
		'''Value of variable $DATE_STR'''
		return self._instance.DateStr

	@property
	def his_idx_ofs(self) -> int:
		'''Value of variable $HIS_IDX_OFS'''
		return self._instance.HisIdxOfs

	@property
	def hist_data(self) -> typing.List[HistEleVariableType]:
		'''Value of variable $HIST_DATA'''
		return [HistEleVariableType(x) for x in self._instance.HistData]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HistDayVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
