import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbgErrlogVariableType as dbg_errlog_variable_type

class DbgErrlogVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbg_errlog_variable_type()
		else:
			self._instance = _internal
	@property
	def num_errors(self) -> int:
		return self._instance.NumErrors
	@property
	def error_ids(self) -> typing.List[int]:
		return self._instance.ErrorIds
	@property
	def run_once(self) -> int:
		return self._instance.RunOnce
	@property
	def syslogstop(self) -> int:
		return self._instance.Syslogstop
	@property
	def syslogerrid(self) -> int:
		return self._instance.Syslogerrid
	@property
	def prev_mode(self) -> int:
		return self._instance.PrevMode
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
