import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MfrqGrpVariableType as mfrq_grp_variable_type

class MfrqGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mfrq_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def act_axis(self) -> int:
		return self._instance.ActAxis
	@property
	def upd_date(self) -> typing.List[str]:
		return self._instance.UpdDate
	@property
	def ave_psd(self) -> typing.List[float]:
		return self._instance.AvePsd
	@property
	def freq_cnt(self) -> typing.List[int]:
		return self._instance.FreqCnt
	@property
	def last_date(self) -> typing.List[int]:
		return self._instance.LastDate
	@property
	def run_task(self) -> typing.List[str]:
		return self._instance.RunTask
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
