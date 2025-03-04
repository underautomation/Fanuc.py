import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DryrunVariableType as dryrun_variable_type

class DryrunVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dryrun_variable_type()
		else:
			self._instance = _internal
	@property
	def dryrun_enb(self) -> bool:
		return self._instance.DryrunEnb
	@property
	def num_port(self) -> int:
		return self._instance.NumPort
	@property
	def num_sub(self) -> int:
		return self._instance.NumSub
	@property
	def state(self) -> int:
		return self._instance.State
	@property
	def tcol_syspt(self) -> int:
		return self._instance.TcolSyspt
	@property
	def pmc_syspt(self) -> int:
		return self._instance.PmcSyspt
	@property
	def grp_mask(self) -> int:
		return self._instance.GrpMask
	@property
	def step_motion(self) -> int:
		return self._instance.StepMotion
	@property
	def log_info(self) -> int:
		return self._instance.LogInfo
	@property
	def tcol_save(self) -> int:
		return self._instance.TcolSave
	@property
	def fltr_empty(self) -> bool:
		return self._instance.FltrEmpty
	@property
	def prod_start(self) -> bool:
		return self._instance.ProdStart
	@property
	def estop_dsbl(self) -> bool:
		return self._instance.EstopDsbl
	@property
	def pow_recov(self) -> bool:
		return self._instance.PowRecov
	@property
	def opr_dsbl(self) -> bool:
		return self._instance.OprDsbl
	@property
	def saw_prog(self) -> str:
		return self._instance.SawProg
	@property
	def init_prog(self) -> str:
		return self._instance.InitProg
	@property
	def resume_type(self) -> int:
		return self._instance.ResumeType
	@property
	def dist_diff(self) -> float:
		return self._instance.DistDiff
	@property
	def ornt_diff(self) -> float:
		return self._instance.OrntDiff
	@property
	def dist_rec(self) -> float:
		return self._instance.DistRec
	@property
	def ornt_rec(self) -> float:
		return self._instance.OrntRec
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
