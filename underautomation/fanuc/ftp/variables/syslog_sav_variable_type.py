import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SyslogSavVariableType as syslog_sav_variable_type

class SyslogSavVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syslog_sav_variable_type()
		else:
			self._instance = _internal
	@property
	def save_blcks(self) -> int:
		return self._instance.SaveBlcks
	@property
	def save_tasks(self) -> int:
		return self._instance.SaveTasks
	@property
	def save_d_cpu(self) -> int:
		return self._instance.SaveDCpu
	@property
	def save_d_siz(self) -> int:
		return self._instance.SaveDSiz
	@property
	def save_d_add(self) -> int:
		return self._instance.SaveDAdd
	@property
	def file_out(self) -> bool:
		return self._instance.FileOut
	@property
	def file_name(self) -> str:
		return self._instance.FileName
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
