import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PgCfgVariableType as pg_cfg_variable_type

class PgCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PG_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pg_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def subtasknum(self) -> int:
		'''Value of variable $SUBTASKNUM'''
		return self._instance.Subtasknum

	@property
	def num_tasks(self) -> int:
		'''Value of variable $NUM_TASKS'''
		return self._instance.NumTasks

	@property
	def jmpwait_upr(self) -> int:
		'''Value of variable $JMPWAIT_UPR'''
		return self._instance.JmpwaitUpr

	@property
	def jmpwait_low(self) -> int:
		'''Value of variable $JMPWAIT_LOW'''
		return self._instance.JmpwaitLow

	@property
	def fast_mode(self) -> int:
		'''Value of variable $FAST_MODE'''
		return self._instance.FastMode

	@property
	def rcvfail_cnt(self) -> int:
		'''Value of variable $RCVFAIL_CNT'''
		return self._instance.RcvfailCnt

	@property
	def waitrel_cfg(self) -> int:
		'''Value of variable $WAITREL_CFG'''
		return self._instance.WaitrelCfg

	@property
	def acc_ctrl(self) -> int:
		'''Value of variable $ACC_CTRL'''
		return self._instance.AccCtrl

	@property
	def cnt_ctrl(self) -> int:
		'''Value of variable $CNT_CTRL'''
		return self._instance.CntCtrl

	@property
	def ignr_pls(self) -> int:
		'''Value of variable $IGNR_PLS'''
		return self._instance.IgnrPls

	@property
	def dbtb_stptyp(self) -> int:
		'''Value of variable $DBTB_STPTYP'''
		return self._instance.DbtbStptyp

	@property
	def bwd_cfg(self) -> int:
		'''Value of variable $BWD_CFG'''
		return self._instance.BwdCfg

	@property
	def resume_cfg(self) -> int:
		'''Value of variable $RESUME_CFG'''
		return self._instance.ResumeCfg

	@property
	def igpaus_pri(self) -> int:
		'''Value of variable $IGPAUS_PRI'''
		return self._instance.IgpausPri

	@property
	def mtnln_cfg(self) -> int:
		'''Value of variable $MTNLN_CFG'''
		return self._instance.MtnlnCfg

	@property
	def paus_rtn(self) -> int:
		'''Value of variable $PAUS_RTN'''
		return self._instance.PausRtn

	@property
	def nomotn_pr(self) -> bool:
		'''Value of variable $NOMOTN_PR'''
		return self._instance.NomotnPr

	@property
	def speed_up(self) -> int:
		'''Value of variable $SPEED_UP'''
		return self._instance.SpeedUp

	@property
	def shadow_stk(self) -> int:
		'''Value of variable $SHADOW_STK'''
		return self._instance.ShadowStk

	@property
	def reserve1(self) -> int:
		'''Value of variable $RESERVE1'''
		return self._instance.Reserve1

	@property
	def reserve2(self) -> int:
		'''Value of variable $RESERVE2'''
		return self._instance.Reserve2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PgCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
