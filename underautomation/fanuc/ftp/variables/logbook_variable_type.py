import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import LogbookVariableType as logbook_variable_type

class LogbookVariableType(GenericVariableType):
	'''Describes the Fanuc type LOGBOOK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = logbook_variable_type()
		else:
			self._instance = _internal

	@property
	def num_er_itm(self) -> int:
		'''Value of variable $NUM_ER_ITM'''
		return self._instance.NumErItm

	@property
	def num_er_typ(self) -> int:
		'''Value of variable $NUM_ER_TYP'''
		return self._instance.NumErTyp

	@property
	def num_rec_typ(self) -> int:
		'''Value of variable $NUM_REC_TYP'''
		return self._instance.NumRecTyp

	@property
	def num_scrn_fl(self) -> int:
		'''Value of variable $NUM_SCRN_FL'''
		return self._instance.NumScrnFl

	@property
	def num_dio(self) -> int:
		'''Value of variable $NUM_DIO'''
		return self._instance.NumDio

	@property
	def sram_margin(self) -> int:
		'''Value of variable $SRAM_MARGIN'''
		return self._instance.SramMargin

	@property
	def dram_margin(self) -> int:
		'''Value of variable $DRAM_MARGIN'''
		return self._instance.DramMargin

	@property
	def option(self) -> int:
		'''Value of variable $OPTION'''
		return self._instance.Option

	@property
	def log_er(self) -> int:
		'''Value of variable $LOG_ER'''
		return self._instance.LogEr

	@property
	def log_ent(self) -> int:
		'''Value of variable $LOG_ENT'''
		return self._instance.LogEnt

	@property
	def log_sel(self) -> int:
		'''Value of variable $LOG_SEL'''
		return self._instance.LogSel

	@property
	def log_win(self) -> int:
		'''Value of variable $LOG_WIN'''
		return self._instance.LogWin

	@property
	def log_menu(self) -> int:
		'''Value of variable $LOG_MENU'''
		return self._instance.LogMenu

	@property
	def log_jgmu(self) -> int:
		'''Value of variable $LOG_JGMU'''
		return self._instance.LogJgmu

	@property
	def log_mnchg(self) -> int:
		'''Value of variable $LOG_MNCHG'''
		return self._instance.LogMnchg

	@property
	def log_fnkey(self) -> int:
		'''Value of variable $LOG_FNKEY'''
		return self._instance.LogFnkey

	@property
	def log_jgky(self) -> int:
		'''Value of variable $LOG_JGKY'''
		return self._instance.LogJgky

	@property
	def log_prgkey(self) -> int:
		'''Value of variable $LOG_PRGKEY'''
		return self._instance.LogPrgkey

	@property
	def log_ufky(self) -> int:
		'''Value of variable $LOG_UFKY'''
		return self._instance.LogUfky

	@property
	def log_ovrky(self) -> int:
		'''Value of variable $LOG_OVRKY'''
		return self._instance.LogOvrky

	@property
	def log_fwdky(self) -> int:
		'''Value of variable $LOG_FWDKY'''
		return self._instance.LogFwdky

	@property
	def log_hldky(self) -> int:
		'''Value of variable $LOG_HLDKY'''
		return self._instance.LogHldky

	@property
	def log_stpky(self) -> int:
		'''Value of variable $LOG_STPKY'''
		return self._instance.LogStpky

	@property
	def log_prvky(self) -> int:
		'''Value of variable $LOG_PRVKY'''
		return self._instance.LogPrvky

	@property
	def log_entky(self) -> int:
		'''Value of variable $LOG_ENTKY'''
		return self._instance.LogEntky

	@property
	def log_itmky(self) -> int:
		'''Value of variable $LOG_ITMKY'''
		return self._instance.LogItmky

	@property
	def log_rstky(self) -> int:
		'''Value of variable $LOG_RSTKY'''
		return self._instance.LogRstky

	@property
	def log_helpky(self) -> int:
		'''Value of variable $LOG_HELPKY'''
		return self._instance.LogHelpky

	@property
	def log_ovr(self) -> int:
		'''Value of variable $LOG_OVR'''
		return self._instance.LogOvr

	@property
	def log_crd(self) -> int:
		'''Value of variable $LOG_CRD'''
		return self._instance.LogCrd

	@property
	def log_step(self) -> int:
		'''Value of variable $LOG_STEP'''
		return self._instance.LogStep

	@property
	def log_grp(self) -> int:
		'''Value of variable $LOG_GRP'''
		return self._instance.LogGrp

	@property
	def log_sgrp(self) -> int:
		'''Value of variable $LOG_SGRP'''
		return self._instance.LogSgrp

	@property
	def log_uf(self) -> int:
		'''Value of variable $LOG_UF'''
		return self._instance.LogUf

	@property
	def log_ut(self) -> int:
		'''Value of variable $LOG_UT'''
		return self._instance.LogUt

	@property
	def log_file(self) -> int:
		'''Value of variable $LOG_FILE'''
		return self._instance.LogFile

	@property
	def log_wtrls(self) -> int:
		'''Value of variable $LOG_WTRLS'''
		return self._instance.LogWtrls

	@property
	def log_pgchg(self) -> int:
		'''Value of variable $LOG_PGCHG'''
		return self._instance.LogPgchg

	@property
	def log_setpos(self) -> int:
		'''Value of variable $LOG_SETPOS'''
		return self._instance.LogSetpos

	@property
	def log_tpky(self) -> int:
		'''Value of variable $LOG_TPKY'''
		return self._instance.LogTpky

	@property
	def log_dio(self) -> int:
		'''Value of variable $LOG_DIO'''
		return self._instance.LogDio

	@property
	def log_stmd(self) -> int:
		'''Value of variable $LOG_STMD'''
		return self._instance.LogStmd

	@property
	def log_focus(self) -> int:
		'''Value of variable $LOG_FOCUS'''
		return self._instance.LogFocus

	@property
	def log_prgexe(self) -> int:
		'''Value of variable $LOG_PRGEXE'''
		return self._instance.LogPrgexe

	@property
	def log_tuikey(self) -> int:
		'''Value of variable $LOG_TUIKEY'''
		return self._instance.LogTuikey

	@property
	def img_ent(self) -> bool:
		'''Value of variable $IMG_ENT'''
		return self._instance.ImgEnt

	@property
	def img_sel(self) -> bool:
		'''Value of variable $IMG_SEL'''
		return self._instance.ImgSel

	@property
	def img_win(self) -> bool:
		'''Value of variable $IMG_WIN'''
		return self._instance.ImgWin

	@property
	def img_fnky(self) -> bool:
		'''Value of variable $IMG_FNKY'''
		return self._instance.ImgFnky

	@property
	def save_file(self) -> str:
		'''Value of variable $SAVE_FILE'''
		return self._instance.SaveFile

	@property
	def scrn_fl(self) -> bool:
		'''Value of variable $SCRN_FL'''
		return self._instance.ScrnFl

	@property
	def scrn_no_ent(self) -> bool:
		'''Value of variable $SCRN_NO_ENT'''
		return self._instance.ScrnNoEnt

	@property
	def analog_tol(self) -> int:
		'''Value of variable $ANALOG_TOL'''
		return self._instance.AnalogTol

	@property
	def available(self) -> int:
		'''Value of variable $AVAILABLE'''
		return self._instance.Available

	@property
	def clear_enb(self) -> bool:
		'''Value of variable $CLEAR_ENB'''
		return self._instance.ClearEnb

	@property
	def dcs_hi1(self) -> int:
		'''Value of variable $DCS_HI1'''
		return self._instance.DcsHi1

	@property
	def dcs_hi2(self) -> int:
		'''Value of variable $DCS_HI2'''
		return self._instance.DcsHi2

	@property
	def dcs_ho1(self) -> int:
		'''Value of variable $DCS_HO1'''
		return self._instance.DcsHo1

	@property
	def dcs_ho2(self) -> int:
		'''Value of variable $DCS_HO2'''
		return self._instance.DcsHo2

	@property
	def dcs_si(self) -> int:
		'''Value of variable $DCS_SI'''
		return self._instance.DcsSi

	@property
	def dcs_so1(self) -> int:
		'''Value of variable $DCS_SO1'''
		return self._instance.DcsSo1

	@property
	def dcs_so2(self) -> int:
		'''Value of variable $DCS_SO2'''
		return self._instance.DcsSo2

	@property
	def dcs_option(self) -> int:
		'''Value of variable $DCS_OPTION'''
		return self._instance.DcsOption

	@property
	def ignr_save(self) -> int:
		'''Value of variable $IGNR_SAVE'''
		return self._instance.IgnrSave

	@property
	def fnkey_fltr(self) -> int:
		'''Value of variable $FNKEY_FLTR'''
		return self._instance.FnkeyFltr

	@property
	def dcs_dev(self) -> int:
		'''Value of variable $DCS_DEV'''
		return self._instance.DcsDev

	@property
	def log_cllb(self) -> int:
		'''Value of variable $LOG_CLLB'''
		return self._instance.LogCllb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogbookVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
