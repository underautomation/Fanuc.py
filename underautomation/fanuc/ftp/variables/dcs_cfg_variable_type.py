import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcsCfgVariableType as dcs_cfg_variable_type

class DcsCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DCS_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcs_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def disp_menu(self) -> int:
		'''Value of variable $DISP_MENU'''
		return self._instance.DispMenu

	@property
	def log_enb(self) -> int:
		'''Value of variable $LOG_ENB'''
		return self._instance.LogEnb

	@property
	def log_len(self) -> int:
		'''Value of variable $LOG_LEN'''
		return self._instance.LogLen

	@property
	def log_file(self) -> str:
		'''Value of variable $LOG_FILE'''
		return self._instance.LogFile

	@property
	def log_id(self) -> int:
		'''Value of variable $LOG_ID'''
		return self._instance.LogId

	@property
	def log_idmax(self) -> int:
		'''Value of variable $LOG_IDMAX'''
		return self._instance.LogIdmax

	@property
	def log_delay(self) -> int:
		'''Value of variable $LOG_DELAY'''
		return self._instance.LogDelay

	@property
	def log_wrt(self) -> int:
		'''Value of variable $LOG_WRT'''
		return self._instance.LogWrt

	@property
	def log_intvl(self) -> int:
		'''Value of variable $LOG_INTVL'''
		return self._instance.LogIntvl

	@property
	def log_event(self) -> int:
		'''Value of variable $LOG_EVENT'''
		return self._instance.LogEvent

	@property
	def log_skip(self) -> int:
		'''Value of variable $LOG_SKIP'''
		return self._instance.LogSkip

	@property
	def test_param1(self) -> int:
		'''Value of variable $TEST_PARAM1'''
		return self._instance.TestParam1

	@property
	def test_param2(self) -> int:
		'''Value of variable $TEST_PARAM2'''
		return self._instance.TestParam2

	@property
	def chk_j_tol(self) -> float:
		'''Value of variable $CHK_J_TOL'''
		return self._instance.ChkJTol

	@property
	def chk_c_tol(self) -> float:
		'''Value of variable $CHK_C_TOL'''
		return self._instance.ChkCTol

	@property
	def safe_spd(self) -> float:
		'''Value of variable $SAFE_SPD'''
		return self._instance.SafeSpd

	@property
	def safe_spd_sv(self) -> float:
		'''Value of variable $SAFE_SPD_SV'''
		return self._instance.SafeSpdSv

	@property
	def exclude(self) -> typing.List[int]:
		'''Value of variable $EXCLUDE'''
		return self._instance.Exclude

	@property
	def spd_only(self) -> typing.List[int]:
		'''Value of variable $SPD_ONLY'''
		return self._instance.SpdOnly

	@property
	def sys_param(self) -> int:
		'''Value of variable $SYS_PARAM'''
		return self._instance.SysParam

	@property
	def protect(self) -> int:
		'''Value of variable $PROTECT'''
		return self._instance.Protect

	@property
	def hi_vrc(self) -> int:
		'''Value of variable $HI_VRC'''
		return self._instance.HiVrc

	@property
	def apply_warn(self) -> int:
		'''Value of variable $APPLY_WARN'''
		return self._instance.ApplyWarn

	@property
	def hide_menu(self) -> int:
		'''Value of variable $HIDE_MENU'''
		return self._instance.HideMenu

	@property
	def hi_vrc_mlt(self) -> typing.List[int]:
		'''Value of variable $HI_VRC_MLT'''
		return self._instance.HiVrcMlt

	@property
	def vrfy_all(self) -> int:
		'''Value of variable $VRFY_ALL'''
		return self._instance.VrfyAll

	@property
	def hi_mate(self) -> int:
		'''Value of variable $HI_MATE'''
		return self._instance.HiMate

	@property
	def ioc_prot(self) -> int:
		'''Value of variable $IOC_PROT'''
		return self._instance.IocProt

	@property
	def ioc_crc1(self) -> int:
		'''Value of variable $IOC_CRC1'''
		return self._instance.IocCrc1

	@property
	def ioc_crc2(self) -> int:
		'''Value of variable $IOC_CRC2'''
		return self._instance.IocCrc2

	@property
	def opi_vrc(self) -> int:
		'''Value of variable $OPI_VRC'''
		return self._instance.OpiVrc

	@property
	def lsr_typ(self) -> int:
		'''Value of variable $LSR_TYP'''
		return self._instance.LsrTyp

	@property
	def dummy43(self) -> int:
		'''Value of variable $DUMMY43'''
		return self._instance.Dummy43

	@property
	def lsr_idx(self) -> int:
		'''Value of variable $LSR_IDX'''
		return self._instance.LsrIdx

	@property
	def sel_tpmode(self) -> int:
		'''Value of variable $SEL_TPMODE'''
		return self._instance.SelTpmode

	@property
	def cnstcy_prot(self) -> int:
		'''Value of variable $CNSTCY_PROT'''
		return self._instance.CnstcyProt

	@property
	def autocnf_typ(self) -> int:
		'''Value of variable $AUTOCNF_TYP'''
		return self._instance.AutocnfTyp

	@property
	def autocnf_idx(self) -> int:
		'''Value of variable $AUTOCNF_IDX'''
		return self._instance.AutocnfIdx

	@property
	def tpmode_opt(self) -> int:
		'''Value of variable $TPMODE_OPT'''
		return self._instance.TpmodeOpt

	@property
	def num_chdg(self) -> int:
		'''Value of variable $NUM_CHDG'''
		return self._instance.NumChdg

	@property
	def dsbl_posspd(self) -> int:
		'''Value of variable $DSBL_POSSPD'''
		return self._instance.DsblPosspd

	@property
	def safio_cpy(self) -> int:
		'''Value of variable $SAFIO_CPY'''
		return self._instance.SafioCpy

	@property
	def tpmode_t2(self) -> bool:
		'''Value of variable $TPMODE_T2'''
		return self._instance.TpmodeT2

	@property
	def enb_vald(self) -> bool:
		'''Value of variable $ENB_VALD'''
		return self._instance.EnbVald

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcsCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
