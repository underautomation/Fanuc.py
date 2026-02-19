import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IrcaCnfVariableType as irca_cnf_variable_type

class IrcaCnfVariableType(GenericVariableType):
	'''Describes the Fanuc type IRCA_CNF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irca_cnf_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def incyc_meas(self) -> int:
		'''Value of variable $INCYC_MEAS'''
		return self._instance.IncycMeas

	@property
	def cyc_ct_meas(self) -> int:
		'''Value of variable $CYC_CT_MEAS'''
		return self._instance.CycCtMeas

	@property
	def cyc_ct_in_t(self) -> int:
		'''Value of variable $CYC_CT_IN_T'''
		return self._instance.CycCtInT

	@property
	def cyc_ct_in_i(self) -> int:
		'''Value of variable $CYC_CT_IN_I'''
		return self._instance.CycCtInI

	@property
	def reg_index(self) -> int:
		'''Value of variable $REG_INDEX'''
		return self._instance.RegIndex

	@property
	def max_day_his(self) -> int:
		'''Value of variable $MAX_DAY_HIS'''
		return self._instance.MaxDayHis

	@property
	def hist_intval(self) -> int:
		'''Value of variable $HIST_INTVAL'''
		return self._instance.HistIntval

	@property
	def rep_intval(self) -> int:
		'''Value of variable $REP_INTVAL'''
		return self._instance.RepIntval

	@property
	def ave_time(self) -> int:
		'''Value of variable $AVE_TIME'''
		return self._instance.AveTime

	@property
	def buff_intval(self) -> int:
		'''Value of variable $BUFF_INTVAL'''
		return self._instance.BuffIntval

	@property
	def scan_intval(self) -> int:
		'''Value of variable $SCAN_INTVAL'''
		return self._instance.ScanIntval

	@property
	def clear_hist(self) -> bool:
		'''Value of variable $CLEAR_HIST'''
		return self._instance.ClearHist

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IrcaCnfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
