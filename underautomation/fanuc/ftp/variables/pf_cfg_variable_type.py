import typing
from underautomation.fanuc.ftp.variables.pf_data_variable_type import PfDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PfCfgVariableType as pf_cfg_variable_type

class PfCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PF_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def cur_group(self) -> int:
		'''Value of variable $CUR_GROUP'''
		return self._instance.CurGroup

	@property
	def ran_groups(self) -> int:
		'''Value of variable $RAN_GROUPS'''
		return self._instance.RanGroups

	@property
	def start_type(self) -> int:
		'''Value of variable $START_TYPE'''
		return self._instance.StartType

	@property
	def total_time(self) -> float:
		'''Value of variable $TOTAL_TIME'''
		return self._instance.TotalTime

	@property
	def total_pwr(self) -> float:
		'''Value of variable $TOTAL_PWR'''
		return self._instance.TotalPwr

	@property
	def ins_pwr(self) -> float:
		'''Value of variable $INS_PWR'''
		return self._instance.InsPwr

	@property
	def regen_pwr(self) -> float:
		'''Value of variable $REGEN_PWR'''
		return self._instance.RegenPwr

	@property
	def ins_regen(self) -> float:
		'''Value of variable $INS_REGEN'''
		return self._instance.InsRegen

	@property
	def exe_date(self) -> str:
		'''Value of variable $EXE_DATE'''
		return self._instance.ExeDate

	@property
	def data_type(self) -> int:
		'''Value of variable $DATA_TYPE'''
		return self._instance.DataType

	@property
	def res_name(self) -> str:
		'''Value of variable $RES_NAME'''
		return self._instance.ResName

	@property
	def montr_rate(self) -> int:
		'''Value of variable $MONTR_RATE'''
		return self._instance.MontrRate

	@property
	def d_pwr_sup(self) -> int:
		'''Value of variable $D_PWR_SUP'''
		return self._instance.DPwrSup

	@property
	def d_pwr_reg(self) -> int:
		'''Value of variable $D_PWR_REG'''
		return self._instance.DPwrReg

	@property
	def rv_lim1(self) -> int:
		'''Value of variable $RV_LIM1'''
		return self._instance.RvLim1

	@property
	def rv_lim2(self) -> int:
		'''Value of variable $RV_LIM2'''
		return self._instance.RvLim2

	@property
	def degree(self) -> int:
		'''Value of variable $DEGREE'''
		return self._instance.Degree

	@property
	def refresh(self) -> int:
		'''Value of variable $REFRESH'''
		return self._instance.Refresh

	@property
	def override(self) -> int:
		'''Value of variable $OVERRIDE'''
		return self._instance.Override

	@property
	def rv_hrs_day(self) -> float:
		'''Value of variable $RV_HRS_DAY'''
		return self._instance.RvHrsDay

	@property
	def rv_days_yr(self) -> int:
		'''Value of variable $RV_DAYS_YR'''
		return self._instance.RvDaysYr

	@property
	def maxsize(self) -> int:
		'''Value of variable $MAXSIZE'''
		return self._instance.Maxsize

	@property
	def summary(self) -> typing.List[PfDataVariableType]:
		'''Value of variable $SUMMARY'''
		return [PfDataVariableType(x) for x in self._instance.Summary]

	@property
	def config_set(self) -> int:
		'''Value of variable $CONFIG_SET'''
		return self._instance.ConfigSet

	@property
	def support(self) -> int:
		'''Value of variable $SUPPORT'''
		return self._instance.Support

	@property
	def last_run(self) -> int:
		'''Value of variable $LAST_RUN'''
		return self._instance.LastRun

	@property
	def rec_style(self) -> int:
		'''Value of variable $REC_STYLE'''
		return self._instance.RecStyle

	@property
	def cmpr_enb(self) -> bool:
		'''Value of variable $CMPR_ENB'''
		return self._instance.CmprEnb

	@property
	def cmpr_dev(self) -> str:
		'''Value of variable $CMPR_DEV'''
		return self._instance.CmprDev

	@property
	def cmpr_dir(self) -> str:
		'''Value of variable $CMPR_DIR'''
		return self._instance.CmprDir

	@property
	def cmpr_suppor(self) -> int:
		'''Value of variable $CMPR_SUPPOR'''
		return self._instance.CmprSuppor

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PfCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
