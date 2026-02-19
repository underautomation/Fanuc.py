import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DbgErrlogVariableType as dbg_errlog_variable_type

class DbgErrlogVariableType(GenericVariableType):
	'''Describes the Fanuc type DBG_ERRLOG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbg_errlog_variable_type()
		else:
			self._instance = _internal

	@property
	def num_errors(self) -> int:
		'''Value of variable $NUM_ERRORS'''
		return self._instance.NumErrors

	@property
	def error_ids(self) -> typing.List[int]:
		'''Value of variable $ERROR_IDS'''
		return self._instance.ErrorIds

	@property
	def run_once(self) -> int:
		'''Value of variable $RUN_ONCE'''
		return self._instance.RunOnce

	@property
	def syslogstop(self) -> int:
		'''Value of variable $SYSLOGSTOP'''
		return self._instance.Syslogstop

	@property
	def syslogerrid(self) -> int:
		'''Value of variable $SYSLOGERRID'''
		return self._instance.Syslogerrid

	@property
	def prev_mode(self) -> int:
		'''Value of variable $PREV_MODE'''
		return self._instance.PrevMode

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DbgErrlogVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
