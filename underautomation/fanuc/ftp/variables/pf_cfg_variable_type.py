import typing
from underautomation.fanuc.ftp.variables.pf_data_variable_type import PfDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PfCfgVariableType as pf_cfg_variable_type

class PfCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def cur_group(self) -> int:
		return self._instance.CurGroup
	@property
	def ran_groups(self) -> int:
		return self._instance.RanGroups
	@property
	def start_type(self) -> int:
		return self._instance.StartType
	@property
	def total_time(self) -> float:
		return self._instance.TotalTime
	@property
	def total_pwr(self) -> float:
		return self._instance.TotalPwr
	@property
	def ins_pwr(self) -> float:
		return self._instance.InsPwr
	@property
	def regen_pwr(self) -> float:
		return self._instance.RegenPwr
	@property
	def ins_regen(self) -> float:
		return self._instance.InsRegen
	@property
	def exe_date(self) -> str:
		return self._instance.ExeDate
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def res_name(self) -> str:
		return self._instance.ResName
	@property
	def montr_rate(self) -> int:
		return self._instance.MontrRate
	@property
	def d_pwr_sup(self) -> int:
		return self._instance.DPwrSup
	@property
	def d_pwr_reg(self) -> int:
		return self._instance.DPwrReg
	@property
	def rv_lim1(self) -> int:
		return self._instance.RvLim1
	@property
	def rv_lim2(self) -> int:
		return self._instance.RvLim2
	@property
	def degree(self) -> int:
		return self._instance.Degree
	@property
	def refresh(self) -> int:
		return self._instance.Refresh
	@property
	def override(self) -> int:
		return self._instance.Override
	@property
	def rv_hrs_day(self) -> float:
		return self._instance.RvHrsDay
	@property
	def rv_days_yr(self) -> int:
		return self._instance.RvDaysYr
	@property
	def maxsize(self) -> int:
		return self._instance.Maxsize
	@property
	def summary(self) -> typing.List[PfDataVariableType]:
		return [PfDataVariableType(x) for x in self._instance.Summary]
	@property
	def config_set(self) -> int:
		return self._instance.ConfigSet
	@property
	def support(self) -> int:
		return self._instance.Support
	@property
	def last_run(self) -> int:
		return self._instance.LastRun
	@property
	def rec_style(self) -> int:
		return self._instance.RecStyle
	@property
	def cmpr_enb(self) -> bool:
		return self._instance.CmprEnb
	@property
	def cmpr_dev(self) -> str:
		return self._instance.CmprDev
	@property
	def cmpr_dir(self) -> str:
		return self._instance.CmprDir
	@property
	def cmpr_suppor(self) -> int:
		return self._instance.CmprSuppor
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
