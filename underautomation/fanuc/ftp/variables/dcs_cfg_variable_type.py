import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcsCfgVariableType as dcs_cfg_variable_type

class DcsCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcs_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def disp_menu(self) -> int:
		return self._instance.DispMenu
	@property
	def log_enb(self) -> int:
		return self._instance.LogEnb
	@property
	def log_len(self) -> int:
		return self._instance.LogLen
	@property
	def log_file(self) -> str:
		return self._instance.LogFile
	@property
	def log_id(self) -> int:
		return self._instance.LogId
	@property
	def log_idmax(self) -> int:
		return self._instance.LogIdmax
	@property
	def log_delay(self) -> int:
		return self._instance.LogDelay
	@property
	def log_wrt(self) -> int:
		return self._instance.LogWrt
	@property
	def log_intvl(self) -> int:
		return self._instance.LogIntvl
	@property
	def log_event(self) -> int:
		return self._instance.LogEvent
	@property
	def log_skip(self) -> int:
		return self._instance.LogSkip
	@property
	def test_param1(self) -> int:
		return self._instance.TestParam1
	@property
	def test_param2(self) -> int:
		return self._instance.TestParam2
	@property
	def chk_j_tol(self) -> float:
		return self._instance.ChkJTol
	@property
	def chk_c_tol(self) -> float:
		return self._instance.ChkCTol
	@property
	def safe_spd(self) -> float:
		return self._instance.SafeSpd
	@property
	def safe_spd_sv(self) -> float:
		return self._instance.SafeSpdSv
	@property
	def exclude(self) -> typing.List[int]:
		return self._instance.Exclude
	@property
	def spd_only(self) -> typing.List[int]:
		return self._instance.SpdOnly
	@property
	def sys_param(self) -> int:
		return self._instance.SysParam
	@property
	def protect(self) -> int:
		return self._instance.Protect
	@property
	def hi_vrc(self) -> int:
		return self._instance.HiVrc
	@property
	def apply_warn(self) -> int:
		return self._instance.ApplyWarn
	@property
	def hide_menu(self) -> int:
		return self._instance.HideMenu
	@property
	def hi_vrc_mlt(self) -> typing.List[int]:
		return self._instance.HiVrcMlt
	@property
	def vrfy_all(self) -> int:
		return self._instance.VrfyAll
	@property
	def hi_mate(self) -> int:
		return self._instance.HiMate
	@property
	def ioc_prot(self) -> int:
		return self._instance.IocProt
	@property
	def ioc_crc1(self) -> int:
		return self._instance.IocCrc1
	@property
	def ioc_crc2(self) -> int:
		return self._instance.IocCrc2
	@property
	def opi_vrc(self) -> int:
		return self._instance.OpiVrc
	@property
	def lsr_typ(self) -> int:
		return self._instance.LsrTyp
	@property
	def dummy43(self) -> int:
		return self._instance.Dummy43
	@property
	def lsr_idx(self) -> int:
		return self._instance.LsrIdx
	@property
	def sel_tpmode(self) -> int:
		return self._instance.SelTpmode
	@property
	def cnstcy_prot(self) -> int:
		return self._instance.CnstcyProt
	@property
	def autocnf_typ(self) -> int:
		return self._instance.AutocnfTyp
	@property
	def autocnf_idx(self) -> int:
		return self._instance.AutocnfIdx
	@property
	def tpmode_opt(self) -> int:
		return self._instance.TpmodeOpt
	@property
	def num_chdg(self) -> int:
		return self._instance.NumChdg
	@property
	def dsbl_posspd(self) -> int:
		return self._instance.DsblPosspd
	@property
	def safio_cpy(self) -> int:
		return self._instance.SafioCpy
	@property
	def tpmode_t2(self) -> bool:
		return self._instance.TpmodeT2
	@property
	def enb_vald(self) -> bool:
		return self._instance.EnbVald
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
