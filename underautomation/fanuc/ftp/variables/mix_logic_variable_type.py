import typing
from underautomation.fanuc.ftp.variables.tcol_line_variable_type import TcolLineVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MixLogicVariableType as mix_logic_variable_type

class MixLogicVariableType(GenericVariableType):
	'''Describes the Fanuc type MIX_LOGIC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mix_logic_variable_type()
		else:
			self._instance = _internal

	@property
	def use_flg(self) -> bool:
		'''Value of variable $USE_FLG'''
		return self._instance.UseFlg

	@property
	def use_mkr(self) -> bool:
		'''Value of variable $USE_MKR'''
		return self._instance.UseMkr

	@property
	def use_tcol(self) -> bool:
		'''Value of variable $USE_TCOL'''
		return self._instance.UseTcol

	@property
	def use_tcolsim(self) -> bool:
		'''Value of variable $USE_TCOLSIM'''
		return self._instance.UseTcolsim

	@property
	def num_flg(self) -> int:
		'''Value of variable $NUM_FLG'''
		return self._instance.NumFlg

	@property
	def num_mkr(self) -> int:
		'''Value of variable $NUM_MKR'''
		return self._instance.NumMkr

	@property
	def num_bg(self) -> int:
		'''Value of variable $NUM_BG'''
		return self._instance.NumBg

	@property
	def num_scan(self) -> int:
		'''Value of variable $NUM_SCAN'''
		return self._instance.NumScan

	@property
	def maxnum_scan(self) -> int:
		'''Value of variable $MAXNUM_SCAN'''
		return self._instance.MaxnumScan

	@property
	def minnum_scan(self) -> int:
		'''Value of variable $MINNUM_SCAN'''
		return self._instance.MinnumScan

	@property
	def item_count(self) -> int:
		'''Value of variable $ITEM_COUNT'''
		return self._instance.ItemCount

	@property
	def proc_time(self) -> int:
		'''Value of variable $PROC_TIME'''
		return self._instance.ProcTime

	@property
	def max_tmr_val(self) -> int:
		'''Value of variable $MAX_TMR_VAL'''
		return self._instance.MaxTmrVal

	@property
	def tcol_line(self) -> TcolLineVariableType:
		'''Value of variable $TCOL_LINE'''
		return TcolLineVariableType(self._instance.TcolLine)

	@property
	def tcol_enb(self) -> bool:
		'''Value of variable $TCOL_ENB'''
		return self._instance.TcolEnb

	@property
	def tcol_sim(self) -> bool:
		'''Value of variable $TCOL_SIM'''
		return self._instance.TcolSim

	@property
	def tcol_stat(self) -> bool:
		'''Value of variable $TCOL_STAT'''
		return self._instance.TcolStat

	@property
	def save_idx(self) -> int:
		'''Value of variable $SAVE_IDX'''
		return self._instance.SaveIdx

	@property
	def save_line(self) -> TcolLineVariableType:
		'''Value of variable $SAVE_LINE'''
		return TcolLineVariableType(self._instance.SaveLine)

	@property
	def tcol_warn(self) -> bool:
		'''Value of variable $TCOL_WARN'''
		return self._instance.TcolWarn

	@property
	def bg_hitem(self) -> int:
		'''Value of variable $BG_HITEM'''
		return self._instance.BgHitem

	@property
	def inst_chk(self) -> bool:
		'''Value of variable $INST_CHK'''
		return self._instance.InstChk

	@property
	def spec_time(self) -> int:
		'''Value of variable $SPEC_TIME'''
		return self._instance.SpecTime

	@property
	def max_prtime(self) -> int:
		'''Value of variable $MAX_PRTIME'''
		return self._instance.MaxPrtime

	@property
	def min_prtime(self) -> int:
		'''Value of variable $MIN_PRTIME'''
		return self._instance.MinPrtime

	@property
	def tcol_opt(self) -> int:
		'''Value of variable $TCOL_OPT'''
		return self._instance.TcolOpt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MixLogicVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
