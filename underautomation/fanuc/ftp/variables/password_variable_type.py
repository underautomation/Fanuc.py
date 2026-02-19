import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PasswordVariableType as password_variable_type

class PasswordVariableType(GenericVariableType):
	'''Describes the Fanuc type PASSWORD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = password_variable_type()
		else:
			self._instance = _internal

	@property
	def time_out(self) -> typing.List[int]:
		'''Value of variable $TIME_OUT'''
		return self._instance.TimeOut

	@property
	def curr_level(self) -> typing.List[int]:
		'''Value of variable $CURR_LEVEL'''
		return self._instance.CurrLevel

	@property
	def curr_user(self) -> typing.List[int]:
		'''Value of variable $CURR_USER'''
		return self._instance.CurrUser

	@property
	def num_users(self) -> int:
		'''Value of variable $NUM_USERS'''
		return self._instance.NumUsers

	@property
	def stop_tpchg(self) -> int:
		'''Value of variable $STOP_TPCHG'''
		return self._instance.StopTpchg

	@property
	def log_events(self) -> bool:
		'''Value of variable $LOG_EVENTS'''
		return self._instance.LogEvents

	@property
	def levels(self) -> typing.List[int]:
		'''Value of variable $LEVELS'''
		return self._instance.Levels

	@property
	def count_down(self) -> typing.List[int]:
		'''Value of variable $COUNT_DOWN'''
		return self._instance.CountDown

	@property
	def enb_pcmpwd(self) -> bool:
		'''Value of variable $ENB_PCMPWD'''
		return self._instance.EnbPcmpwd

	@property
	def dvpcm_login(self) -> int:
		'''Value of variable $DVPCM_LOGIN'''
		return self._instance.DvpcmLogin

	@property
	def pcm_login(self) -> typing.List[int]:
		'''Value of variable $PCM_LOGIN'''
		return self._instance.PcmLogin

	@property
	def enb_lvchk(self) -> bool:
		'''Value of variable $ENB_LVCHK'''
		return self._instance.EnbLvchk

	@property
	def enb_fullmn(self) -> bool:
		'''Value of variable $ENB_FULLMN'''
		return self._instance.EnbFullmn

	@property
	def enb_timext(self) -> bool:
		'''Value of variable $ENB_TIMEXT'''
		return self._instance.EnbTimext

	@property
	def enb_cntdwn(self) -> bool:
		'''Value of variable $ENB_CNTDWN'''
		return self._instance.EnbCntdwn

	@property
	def enb_menu(self) -> bool:
		'''Value of variable $ENB_MENU'''
		return self._instance.EnbMenu

	@property
	def autologin(self) -> bool:
		'''Value of variable $AUTOLOGIN'''
		return self._instance.Autologin

	@property
	def enb_cfg_dsp(self) -> bool:
		'''Value of variable $ENB_CFG_DSP'''
		return self._instance.EnbCfgDsp

	@property
	def enb_rls_dsp(self) -> bool:
		'''Value of variable $ENB_RLS_DSP'''
		return self._instance.EnbRlsDsp

	@property
	def ulog_events(self) -> bool:
		'''Value of variable $ULOG_EVENTS'''
		return self._instance.UlogEvents

	@property
	def burybanmenu(self) -> bool:
		'''Value of variable $BURYBANMENU'''
		return self._instance.Burybanmenu

	@property
	def enb_gilogin(self) -> bool:
		'''Value of variable $ENB_GILOGIN'''
		return self._instance.EnbGilogin

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PasswordVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
