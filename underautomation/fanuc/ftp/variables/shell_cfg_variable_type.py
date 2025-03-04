import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ShellCfgVariableType as shell_cfg_variable_type

class ShellCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def job_base(self) -> int:
		return self._instance.JobBase
	@property
	def rsr_enable(self) -> typing.List[bool]:
		return self._instance.RsrEnable
	@property
	def num_rsr(self) -> typing.List[int]:
		return self._instance.NumRsr
	@property
	def rsr1_name(self) -> str:
		return self._instance.Rsr1Name
	@property
	def rsr2_name(self) -> str:
		return self._instance.Rsr2Name
	@property
	def rsr3_name(self) -> str:
		return self._instance.Rsr3Name
	@property
	def rsr4_name(self) -> str:
		return self._instance.Rsr4Name
	@property
	def rsr5_name(self) -> str:
		return self._instance.Rsr5Name
	@property
	def rsr6_name(self) -> str:
		return self._instance.Rsr6Name
	@property
	def rsr7_name(self) -> str:
		return self._instance.Rsr7Name
	@property
	def rsr8_name(self) -> str:
		return self._instance.Rsr8Name
	@property
	def job_root(self) -> str:
		return self._instance.JobRoot
	@property
	def cont_only(self) -> bool:
		return self._instance.ContOnly
	@property
	def use_abort(self) -> bool:
		return self._instance.UseAbort
	@property
	def rsr_ackenbl(self) -> bool:
		return self._instance.RsrAckenbl
	@property
	def invert_chk(self) -> bool:
		return self._instance.InvertChk
	@property
	def uop_sel_sta(self) -> bool:
		return self._instance.UopSelSta
	@property
	def rsr_ack_pul(self) -> int:
		return self._instance.RsrAckPul
	@property
	def com_timeout(self) -> int:
		return self._instance.ComTimeout
	@property
	def pns_enable(self) -> bool:
		return self._instance.PnsEnable
	@property
	def shell_name(self) -> str:
		return self._instance.ShellName
	@property
	def start_mode(self) -> int:
		return self._instance.StartMode
	@property
	def tpfwd_karel(self) -> bool:
		return self._instance.TpfwdKarel
	@property
	def err_report(self) -> bool:
		return self._instance.ErrReport
	@property
	def options(self) -> int:
		return self._instance.Options
	@property
	def que_enable(self) -> bool:
		return self._instance.QueEnable
	@property
	def prodstartyp(self) -> int:
		return self._instance.Prodstartyp
	@property
	def cstopi_all(self) -> bool:
		return self._instance.CstopiAll
	@property
	def shell_ext(self) -> bool:
		return self._instance.ShellExt
	@property
	def sel_type(self) -> int:
		return self._instance.SelType
	@property
	def ext_sem1(self) -> int:
		return self._instance.ExtSem1
	@property
	def ext_sem2(self) -> int:
		return self._instance.ExtSem2
	@property
	def maint_styl(self) -> bool:
		return self._instance.MaintStyl
	@property
	def isol_enb(self) -> bool:
		return self._instance.IsolEnb
	@property
	def di_chktrig(self) -> int:
		return self._instance.DiChktrig
	@property
	def prod_mode(self) -> int:
		return self._instance.ProdMode
	@property
	def init_tmo(self) -> int:
		return self._instance.InitTmo
	@property
	def manrq_tmo(self) -> int:
		return self._instance.ManrqTmo
	@property
	def extend_enb(self) -> int:
		return self._instance.ExtendEnb
	@property
	def keyswitch(self) -> bool:
		return self._instance.Keyswitch
	@property
	def startchktyp(self) -> int:
		return self._instance.Startchktyp
	@property
	def heartbeatms(self) -> int:
		return self._instance.Heartbeatms
	@property
	def perm_level(self) -> int:
		return self._instance.PermLevel
	@property
	def temp_level(self) -> int:
		return self._instance.TempLevel
	@property
	def ustart_ft(self) -> bool:
		return self._instance.UstartFt
	@property
	def start_sig(self) -> int:
		return self._instance.StartSig
	@property
	def do_home_sop(self) -> bool:
		return self._instance.DoHomeSop
	@property
	def refps_pr_id(self) -> int:
		return self._instance.RefpsPrId
	@property
	def dis_strtchk(self) -> bool:
		return self._instance.DisStrtchk
	@property
	def custom(self) -> int:
		return self._instance.Custom
	@property
	def e_recov_msk(self) -> int:
		return self._instance.ERecovMsk
	@property
	def set_iocmnt(self) -> bool:
		return self._instance.SetIocmnt
	@property
	def cstopi_all2(self) -> bool:
		return self._instance.CstopiAll2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
