import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PgCfgVariableType as pg_cfg_variable_type

class PgCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pg_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def subtasknum(self) -> int:
		return self._instance.Subtasknum
	@property
	def num_tasks(self) -> int:
		return self._instance.NumTasks
	@property
	def jmpwait_upr(self) -> int:
		return self._instance.JmpwaitUpr
	@property
	def jmpwait_low(self) -> int:
		return self._instance.JmpwaitLow
	@property
	def fast_mode(self) -> int:
		return self._instance.FastMode
	@property
	def rcvfail_cnt(self) -> int:
		return self._instance.RcvfailCnt
	@property
	def waitrel_cfg(self) -> int:
		return self._instance.WaitrelCfg
	@property
	def acc_ctrl(self) -> int:
		return self._instance.AccCtrl
	@property
	def cnt_ctrl(self) -> int:
		return self._instance.CntCtrl
	@property
	def ignr_pls(self) -> int:
		return self._instance.IgnrPls
	@property
	def dbtb_stptyp(self) -> int:
		return self._instance.DbtbStptyp
	@property
	def bwd_cfg(self) -> int:
		return self._instance.BwdCfg
	@property
	def resume_cfg(self) -> int:
		return self._instance.ResumeCfg
	@property
	def igpaus_pri(self) -> int:
		return self._instance.IgpausPri
	@property
	def mtnln_cfg(self) -> int:
		return self._instance.MtnlnCfg
	@property
	def paus_rtn(self) -> int:
		return self._instance.PausRtn
	@property
	def nomotn_pr(self) -> bool:
		return self._instance.NomotnPr
	@property
	def speed_up(self) -> int:
		return self._instance.SpeedUp
	@property
	def shadow_stk(self) -> int:
		return self._instance.ShadowStk
	@property
	def reserve1(self) -> int:
		return self._instance.Reserve1
	@property
	def reserve2(self) -> int:
		return self._instance.Reserve2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
