import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DryrunVariableType as dryrun_variable_type

class DryrunVariableType(GenericVariableType):
	'''Describes the Fanuc type DRYRUN_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dryrun_variable_type()
		else:
			self._instance = _internal

	@property
	def dryrun_enb(self) -> bool:
		'''Value of variable $DRYRUN_ENB'''
		return self._instance.DryrunEnb

	@property
	def num_port(self) -> int:
		'''Value of variable $NUM_PORT'''
		return self._instance.NumPort

	@property
	def num_sub(self) -> int:
		'''Value of variable $NUM_SUB'''
		return self._instance.NumSub

	@property
	def state(self) -> int:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def tcol_syspt(self) -> int:
		'''Value of variable $TCOL_SYSPT'''
		return self._instance.TcolSyspt

	@property
	def pmc_syspt(self) -> int:
		'''Value of variable $PMC_SYSPT'''
		return self._instance.PmcSyspt

	@property
	def grp_mask(self) -> int:
		'''Value of variable $GRP_MASK'''
		return self._instance.GrpMask

	@property
	def step_motion(self) -> int:
		'''Value of variable $STEP_MOTION'''
		return self._instance.StepMotion

	@property
	def log_info(self) -> int:
		'''Value of variable $LOG_INFO'''
		return self._instance.LogInfo

	@property
	def tcol_save(self) -> int:
		'''Value of variable $TCOL_SAVE'''
		return self._instance.TcolSave

	@property
	def fltr_empty(self) -> bool:
		'''Value of variable $FLTR_EMPTY'''
		return self._instance.FltrEmpty

	@property
	def prod_start(self) -> bool:
		'''Value of variable $PROD_START'''
		return self._instance.ProdStart

	@property
	def estop_dsbl(self) -> bool:
		'''Value of variable $ESTOP_DSBL'''
		return self._instance.EstopDsbl

	@property
	def pow_recov(self) -> bool:
		'''Value of variable $POW_RECOV'''
		return self._instance.PowRecov

	@property
	def opr_dsbl(self) -> bool:
		'''Value of variable $OPR_DSBL'''
		return self._instance.OprDsbl

	@property
	def saw_prog(self) -> str:
		'''Value of variable $SAW_PROG'''
		return self._instance.SawProg

	@property
	def init_prog(self) -> str:
		'''Value of variable $INIT_PROG'''
		return self._instance.InitProg

	@property
	def resume_type(self) -> int:
		'''Value of variable $RESUME_TYPE'''
		return self._instance.ResumeType

	@property
	def dist_diff(self) -> float:
		'''Value of variable $DIST_DIFF'''
		return self._instance.DistDiff

	@property
	def ornt_diff(self) -> float:
		'''Value of variable $ORNT_DIFF'''
		return self._instance.OrntDiff

	@property
	def dist_rec(self) -> float:
		'''Value of variable $DIST_REC'''
		return self._instance.DistRec

	@property
	def ornt_rec(self) -> float:
		'''Value of variable $ORNT_REC'''
		return self._instance.OrntRec

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DryrunVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
