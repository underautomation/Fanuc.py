import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SntpCfgVariableType as sntp_cfg_variable_type

class SntpCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type SNTP_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sntp_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def server(self) -> str:
		'''Value of variable $SERVER'''
		return self._instance.Server

	@property
	def time_win(self) -> int:
		'''Value of variable $TIME_WIN'''
		return self._instance.TimeWin

	@property
	def tz_index(self) -> int:
		'''Value of variable $TZ_INDEX'''
		return self._instance.TzIndex

	@property
	def tz_offset(self) -> int:
		'''Value of variable $TZ_OFFSET'''
		return self._instance.TzOffset

	@property
	def cur_offset(self) -> int:
		'''Value of variable $CUR_OFFSET'''
		return self._instance.CurOffset

	@property
	def dst(self) -> bool:
		'''Value of variable $DST'''
		return self._instance.Dst

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SntpCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
