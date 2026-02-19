import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ShellCfgVariableType as shell_cfg_variable_type

class ShellCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type SHELL_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def job_base(self) -> int:
		'''Value of variable $JOB_BASE'''
		return self._instance.JobBase

	@property
	def rsr_enable(self) -> typing.List[bool]:
		'''Value of variable $RSR_ENABLE'''
		return self._instance.RsrEnable

	@property
	def num_rsr(self) -> typing.List[int]:
		'''Value of variable $NUM_RSR'''
		return self._instance.NumRsr

	@property
	def rsr1_name(self) -> str:
		'''Value of variable $RSR1_NAME'''
		return self._instance.Rsr1Name

	@property
	def rsr2_name(self) -> str:
		'''Value of variable $RSR2_NAME'''
		return self._instance.Rsr2Name

	@property
	def rsr3_name(self) -> str:
		'''Value of variable $RSR3_NAME'''
		return self._instance.Rsr3Name

	@property
	def rsr4_name(self) -> str:
		'''Value of variable $RSR4_NAME'''
		return self._instance.Rsr4Name

	@property
	def rsr5_name(self) -> str:
		'''Value of variable $RSR5_NAME'''
		return self._instance.Rsr5Name

	@property
	def rsr6_name(self) -> str:
		'''Value of variable $RSR6_NAME'''
		return self._instance.Rsr6Name

	@property
	def rsr7_name(self) -> str:
		'''Value of variable $RSR7_NAME'''
		return self._instance.Rsr7Name

	@property
	def rsr8_name(self) -> str:
		'''Value of variable $RSR8_NAME'''
		return self._instance.Rsr8Name

	@property
	def job_root(self) -> str:
		'''Value of variable $JOB_ROOT'''
		return self._instance.JobRoot

	@property
	def cont_only(self) -> bool:
		'''Value of variable $CONT_ONLY'''
		return self._instance.ContOnly

	@property
	def use_abort(self) -> bool:
		'''Value of variable $USE_ABORT'''
		return self._instance.UseAbort

	@property
	def rsr_ackenbl(self) -> bool:
		'''Value of variable $RSR_ACKENBL'''
		return self._instance.RsrAckenbl

	@property
	def invert_chk(self) -> bool:
		'''Value of variable $INVERT_CHK'''
		return self._instance.InvertChk

	@property
	def uop_sel_sta(self) -> bool:
		'''Value of variable $UOP_SEL_STA'''
		return self._instance.UopSelSta

	@property
	def rsr_ack_pul(self) -> int:
		'''Value of variable $RSR_ACK_PUL'''
		return self._instance.RsrAckPul

	@property
	def com_timeout(self) -> int:
		'''Value of variable $COM_TIMEOUT'''
		return self._instance.ComTimeout

	@property
	def pns_enable(self) -> bool:
		'''Value of variable $PNS_ENABLE'''
		return self._instance.PnsEnable

	@property
	def shell_name(self) -> str:
		'''Value of variable $SHELL_NAME'''
		return self._instance.ShellName

	@property
	def start_mode(self) -> int:
		'''Value of variable $START_MODE'''
		return self._instance.StartMode

	@property
	def tpfwd_karel(self) -> bool:
		'''Value of variable $TPFWD_KAREL'''
		return self._instance.TpfwdKarel

	@property
	def err_report(self) -> bool:
		'''Value of variable $ERR_REPORT'''
		return self._instance.ErrReport

	@property
	def options(self) -> int:
		'''Value of variable $OPTIONS'''
		return self._instance.Options

	@property
	def que_enable(self) -> bool:
		'''Value of variable $QUE_ENABLE'''
		return self._instance.QueEnable

	@property
	def prodstartyp(self) -> int:
		'''Value of variable $PRODSTARTYP'''
		return self._instance.Prodstartyp

	@property
	def cstopi_all(self) -> bool:
		'''Value of variable $CSTOPI_ALL'''
		return self._instance.CstopiAll

	@property
	def shell_ext(self) -> bool:
		'''Value of variable $SHELL_EXT'''
		return self._instance.ShellExt

	@property
	def sel_type(self) -> int:
		'''Value of variable $SEL_TYPE'''
		return self._instance.SelType

	@property
	def ext_sem1(self) -> int:
		'''Value of variable $EXT_SEM1'''
		return self._instance.ExtSem1

	@property
	def ext_sem2(self) -> int:
		'''Value of variable $EXT_SEM2'''
		return self._instance.ExtSem2

	@property
	def maint_styl(self) -> bool:
		'''Value of variable $MAINT_STYL'''
		return self._instance.MaintStyl

	@property
	def isol_enb(self) -> bool:
		'''Value of variable $ISOL_ENB'''
		return self._instance.IsolEnb

	@property
	def di_chktrig(self) -> int:
		'''Value of variable $DI_CHKTRIG'''
		return self._instance.DiChktrig

	@property
	def prod_mode(self) -> int:
		'''Value of variable $PROD_MODE'''
		return self._instance.ProdMode

	@property
	def init_tmo(self) -> int:
		'''Value of variable $INIT_TMO'''
		return self._instance.InitTmo

	@property
	def manrq_tmo(self) -> int:
		'''Value of variable $MANRQ_TMO'''
		return self._instance.ManrqTmo

	@property
	def extend_enb(self) -> int:
		'''Value of variable $EXTEND_ENB'''
		return self._instance.ExtendEnb

	@property
	def keyswitch(self) -> bool:
		'''Value of variable $KEYSWITCH'''
		return self._instance.Keyswitch

	@property
	def startchktyp(self) -> int:
		'''Value of variable $STARTCHKTYP'''
		return self._instance.Startchktyp

	@property
	def heartbeatms(self) -> int:
		'''Value of variable $HEARTBEATMS'''
		return self._instance.Heartbeatms

	@property
	def perm_level(self) -> int:
		'''Value of variable $PERM_LEVEL'''
		return self._instance.PermLevel

	@property
	def temp_level(self) -> int:
		'''Value of variable $TEMP_LEVEL'''
		return self._instance.TempLevel

	@property
	def ustart_ft(self) -> bool:
		'''Value of variable $USTART_FT'''
		return self._instance.UstartFt

	@property
	def start_sig(self) -> int:
		'''Value of variable $START_SIG'''
		return self._instance.StartSig

	@property
	def do_home_sop(self) -> bool:
		'''Value of variable $DO_HOME_SOP'''
		return self._instance.DoHomeSop

	@property
	def refps_pr_id(self) -> int:
		'''Value of variable $REFPS_PR_ID'''
		return self._instance.RefpsPrId

	@property
	def dis_strtchk(self) -> bool:
		'''Value of variable $DIS_STRTCHK'''
		return self._instance.DisStrtchk

	@property
	def custom(self) -> int:
		'''Value of variable $CUSTOM'''
		return self._instance.Custom

	@property
	def e_recov_msk(self) -> int:
		'''Value of variable $E_RECOV_MSK'''
		return self._instance.ERecovMsk

	@property
	def set_iocmnt(self) -> bool:
		'''Value of variable $SET_IOCMNT'''
		return self._instance.SetIocmnt

	@property
	def cstopi_all2(self) -> bool:
		'''Value of variable $CSTOPI_ALL2'''
		return self._instance.CstopiAll2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
