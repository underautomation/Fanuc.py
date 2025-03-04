import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SyslogVariableType as syslog_variable_type

class SyslogVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syslog_variable_type()
		else:
			self._instance = _internal
	@property
	def size(self) -> int:
		return self._instance.Size
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def address(self) -> int:
		return self._instance.Address
	@property
	def data_size(self) -> int:
		return self._instance.DataSize
	@property
	def comp_value(self) -> int:
		return self._instance.CompValue
	@property
	def stop_mode(self) -> int:
		return self._instance.StopMode
	@property
	def curr_value(self) -> int:
		return self._instance.CurrValue
	@property
	def flog_id_lo(self) -> int:
		return self._instance.FlogIdLo
	@property
	def flog_id_hi(self) -> int:
		return self._instance.FlogIdHi
	@property
	def flog_id_in(self) -> bool:
		return self._instance.FlogIdIn
	@property
	def file_out(self) -> bool:
		return self._instance.FileOut
	@property
	def file_name(self) -> str:
		return self._instance.FileName
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
