import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LogbookVariableType as logbook_variable_type

class LogbookVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = logbook_variable_type()
		else:
			self._instance = _internal
	@property
	def num_er_itm(self) -> int:
		return self._instance.NumErItm
	@property
	def num_er_typ(self) -> int:
		return self._instance.NumErTyp
	@property
	def num_rec_typ(self) -> int:
		return self._instance.NumRecTyp
	@property
	def num_scrn_fl(self) -> int:
		return self._instance.NumScrnFl
	@property
	def num_dio(self) -> int:
		return self._instance.NumDio
	@property
	def sram_margin(self) -> int:
		return self._instance.SramMargin
	@property
	def dram_margin(self) -> int:
		return self._instance.DramMargin
	@property
	def option(self) -> int:
		return self._instance.Option
	@property
	def log_er(self) -> int:
		return self._instance.LogEr
	@property
	def log_ent(self) -> int:
		return self._instance.LogEnt
	@property
	def log_sel(self) -> int:
		return self._instance.LogSel
	@property
	def log_win(self) -> int:
		return self._instance.LogWin
	@property
	def log_menu(self) -> int:
		return self._instance.LogMenu
	@property
	def log_jgmu(self) -> int:
		return self._instance.LogJgmu
	@property
	def log_mnchg(self) -> int:
		return self._instance.LogMnchg
	@property
	def log_fnkey(self) -> int:
		return self._instance.LogFnkey
	@property
	def log_jgky(self) -> int:
		return self._instance.LogJgky
	@property
	def log_prgkey(self) -> int:
		return self._instance.LogPrgkey
	@property
	def log_ufky(self) -> int:
		return self._instance.LogUfky
	@property
	def log_ovrky(self) -> int:
		return self._instance.LogOvrky
	@property
	def log_fwdky(self) -> int:
		return self._instance.LogFwdky
	@property
	def log_hldky(self) -> int:
		return self._instance.LogHldky
	@property
	def log_stpky(self) -> int:
		return self._instance.LogStpky
	@property
	def log_prvky(self) -> int:
		return self._instance.LogPrvky
	@property
	def log_entky(self) -> int:
		return self._instance.LogEntky
	@property
	def log_itmky(self) -> int:
		return self._instance.LogItmky
	@property
	def log_rstky(self) -> int:
		return self._instance.LogRstky
	@property
	def log_helpky(self) -> int:
		return self._instance.LogHelpky
	@property
	def log_ovr(self) -> int:
		return self._instance.LogOvr
	@property
	def log_crd(self) -> int:
		return self._instance.LogCrd
	@property
	def log_step(self) -> int:
		return self._instance.LogStep
	@property
	def log_grp(self) -> int:
		return self._instance.LogGrp
	@property
	def log_sgrp(self) -> int:
		return self._instance.LogSgrp
	@property
	def log_uf(self) -> int:
		return self._instance.LogUf
	@property
	def log_ut(self) -> int:
		return self._instance.LogUt
	@property
	def log_file(self) -> int:
		return self._instance.LogFile
	@property
	def log_wtrls(self) -> int:
		return self._instance.LogWtrls
	@property
	def log_pgchg(self) -> int:
		return self._instance.LogPgchg
	@property
	def log_setpos(self) -> int:
		return self._instance.LogSetpos
	@property
	def log_tpky(self) -> int:
		return self._instance.LogTpky
	@property
	def log_dio(self) -> int:
		return self._instance.LogDio
	@property
	def log_stmd(self) -> int:
		return self._instance.LogStmd
	@property
	def log_focus(self) -> int:
		return self._instance.LogFocus
	@property
	def log_prgexe(self) -> int:
		return self._instance.LogPrgexe
	@property
	def log_tuikey(self) -> int:
		return self._instance.LogTuikey
	@property
	def img_ent(self) -> bool:
		return self._instance.ImgEnt
	@property
	def img_sel(self) -> bool:
		return self._instance.ImgSel
	@property
	def img_win(self) -> bool:
		return self._instance.ImgWin
	@property
	def img_fnky(self) -> bool:
		return self._instance.ImgFnky
	@property
	def save_file(self) -> str:
		return self._instance.SaveFile
	@property
	def scrn_fl(self) -> bool:
		return self._instance.ScrnFl
	@property
	def scrn_no_ent(self) -> bool:
		return self._instance.ScrnNoEnt
	@property
	def analog_tol(self) -> int:
		return self._instance.AnalogTol
	@property
	def available(self) -> int:
		return self._instance.Available
	@property
	def clear_enb(self) -> bool:
		return self._instance.ClearEnb
	@property
	def dcs_hi1(self) -> int:
		return self._instance.DcsHi1
	@property
	def dcs_hi2(self) -> int:
		return self._instance.DcsHi2
	@property
	def dcs_ho1(self) -> int:
		return self._instance.DcsHo1
	@property
	def dcs_ho2(self) -> int:
		return self._instance.DcsHo2
	@property
	def dcs_si(self) -> int:
		return self._instance.DcsSi
	@property
	def dcs_so1(self) -> int:
		return self._instance.DcsSo1
	@property
	def dcs_so2(self) -> int:
		return self._instance.DcsSo2
	@property
	def dcs_option(self) -> int:
		return self._instance.DcsOption
	@property
	def ignr_save(self) -> int:
		return self._instance.IgnrSave
	@property
	def fnkey_fltr(self) -> int:
		return self._instance.FnkeyFltr
	@property
	def dcs_dev(self) -> int:
		return self._instance.DcsDev
	@property
	def log_cllb(self) -> int:
		return self._instance.LogCllb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
