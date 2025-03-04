import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PasswordVariableType as password_variable_type

class PasswordVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = password_variable_type()
		else:
			self._instance = _internal
	@property
	def time_out(self) -> typing.List[int]:
		return self._instance.TimeOut
	@property
	def curr_level(self) -> typing.List[int]:
		return self._instance.CurrLevel
	@property
	def curr_user(self) -> typing.List[int]:
		return self._instance.CurrUser
	@property
	def num_users(self) -> int:
		return self._instance.NumUsers
	@property
	def stop_tpchg(self) -> int:
		return self._instance.StopTpchg
	@property
	def log_events(self) -> bool:
		return self._instance.LogEvents
	@property
	def levels(self) -> typing.List[int]:
		return self._instance.Levels
	@property
	def count_down(self) -> typing.List[int]:
		return self._instance.CountDown
	@property
	def enb_pcmpwd(self) -> bool:
		return self._instance.EnbPcmpwd
	@property
	def dvpcm_login(self) -> int:
		return self._instance.DvpcmLogin
	@property
	def pcm_login(self) -> typing.List[int]:
		return self._instance.PcmLogin
	@property
	def enb_lvchk(self) -> bool:
		return self._instance.EnbLvchk
	@property
	def enb_fullmn(self) -> bool:
		return self._instance.EnbFullmn
	@property
	def enb_timext(self) -> bool:
		return self._instance.EnbTimext
	@property
	def enb_cntdwn(self) -> bool:
		return self._instance.EnbCntdwn
	@property
	def enb_menu(self) -> bool:
		return self._instance.EnbMenu
	@property
	def autologin(self) -> bool:
		return self._instance.Autologin
	@property
	def enb_cfg_dsp(self) -> bool:
		return self._instance.EnbCfgDsp
	@property
	def enb_rls_dsp(self) -> bool:
		return self._instance.EnbRlsDsp
	@property
	def ulog_events(self) -> bool:
		return self._instance.UlogEvents
	@property
	def burybanmenu(self) -> bool:
		return self._instance.Burybanmenu
	@property
	def enb_gilogin(self) -> bool:
		return self._instance.EnbGilogin
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
