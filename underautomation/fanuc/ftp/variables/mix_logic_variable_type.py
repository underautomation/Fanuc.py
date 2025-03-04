import typing
from underautomation.fanuc.ftp.variables.tcol_line_variable_type import TcolLineVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MixLogicVariableType as mix_logic_variable_type

class MixLogicVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mix_logic_variable_type()
		else:
			self._instance = _internal
	@property
	def use_flg(self) -> bool:
		return self._instance.UseFlg
	@property
	def use_mkr(self) -> bool:
		return self._instance.UseMkr
	@property
	def use_tcol(self) -> bool:
		return self._instance.UseTcol
	@property
	def use_tcolsim(self) -> bool:
		return self._instance.UseTcolsim
	@property
	def num_flg(self) -> int:
		return self._instance.NumFlg
	@property
	def num_mkr(self) -> int:
		return self._instance.NumMkr
	@property
	def num_bg(self) -> int:
		return self._instance.NumBg
	@property
	def num_scan(self) -> int:
		return self._instance.NumScan
	@property
	def maxnum_scan(self) -> int:
		return self._instance.MaxnumScan
	@property
	def minnum_scan(self) -> int:
		return self._instance.MinnumScan
	@property
	def item_count(self) -> int:
		return self._instance.ItemCount
	@property
	def proc_time(self) -> int:
		return self._instance.ProcTime
	@property
	def max_tmr_val(self) -> int:
		return self._instance.MaxTmrVal
	@property
	def tcol_line(self) -> TcolLineVariableType:
		return TcolLineVariableType(self._instance.TcolLine)
	@property
	def tcol_enb(self) -> bool:
		return self._instance.TcolEnb
	@property
	def tcol_sim(self) -> bool:
		return self._instance.TcolSim
	@property
	def tcol_stat(self) -> bool:
		return self._instance.TcolStat
	@property
	def save_idx(self) -> int:
		return self._instance.SaveIdx
	@property
	def save_line(self) -> TcolLineVariableType:
		return TcolLineVariableType(self._instance.SaveLine)
	@property
	def tcol_warn(self) -> bool:
		return self._instance.TcolWarn
	@property
	def bg_hitem(self) -> int:
		return self._instance.BgHitem
	@property
	def inst_chk(self) -> bool:
		return self._instance.InstChk
	@property
	def spec_time(self) -> int:
		return self._instance.SpecTime
	@property
	def max_prtime(self) -> int:
		return self._instance.MaxPrtime
	@property
	def min_prtime(self) -> int:
		return self._instance.MinPrtime
	@property
	def tcol_opt(self) -> int:
		return self._instance.TcolOpt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
