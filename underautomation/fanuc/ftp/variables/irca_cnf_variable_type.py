import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IrcaCnfVariableType as irca_cnf_variable_type

class IrcaCnfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irca_cnf_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def incyc_meas(self) -> int:
		return self._instance.IncycMeas
	@property
	def cyc_ct_meas(self) -> int:
		return self._instance.CycCtMeas
	@property
	def cyc_ct_in_t(self) -> int:
		return self._instance.CycCtInT
	@property
	def cyc_ct_in_i(self) -> int:
		return self._instance.CycCtInI
	@property
	def reg_index(self) -> int:
		return self._instance.RegIndex
	@property
	def max_day_his(self) -> int:
		return self._instance.MaxDayHis
	@property
	def hist_intval(self) -> int:
		return self._instance.HistIntval
	@property
	def rep_intval(self) -> int:
		return self._instance.RepIntval
	@property
	def ave_time(self) -> int:
		return self._instance.AveTime
	@property
	def buff_intval(self) -> int:
		return self._instance.BuffIntval
	@property
	def scan_intval(self) -> int:
		return self._instance.ScanIntval
	@property
	def clear_hist(self) -> bool:
		return self._instance.ClearHist
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
