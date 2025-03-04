import typing
from underautomation.fanuc.ftp.variables.hist_ele_variable_type import HistEleVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HistDayVariableType as hist_day_variable_type

class HistDayVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hist_day_variable_type()
		else:
			self._instance = _internal
	@property
	def date(self) -> int:
		return self._instance.Date
	@property
	def date_str(self) -> str:
		return self._instance.DateStr
	@property
	def his_idx_ofs(self) -> int:
		return self._instance.HisIdxOfs
	@property
	def hist_data(self) -> typing.List[HistEleVariableType]:
		return [HistEleVariableType(x) for x in self._instance.HistData]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
