import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SyslogSavVariableType as syslog_sav_variable_type

class SyslogSavVariableType(GenericVariableType):
	'''Describes the Fanuc type SYSLOG_SAV_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syslog_sav_variable_type()
		else:
			self._instance = _internal

	@property
	def save_blcks(self) -> int:
		'''Value of variable $SAVE_BLCKS'''
		return self._instance.SaveBlcks

	@property
	def save_tasks(self) -> int:
		'''Value of variable $SAVE_TASKS'''
		return self._instance.SaveTasks

	@property
	def save_d_cpu(self) -> int:
		'''Value of variable $SAVE_D_CPU'''
		return self._instance.SaveDCpu

	@property
	def save_d_siz(self) -> int:
		'''Value of variable $SAVE_D_SIZ'''
		return self._instance.SaveDSiz

	@property
	def save_d_add(self) -> int:
		'''Value of variable $SAVE_D_ADD'''
		return self._instance.SaveDAdd

	@property
	def file_out(self) -> bool:
		'''Value of variable $FILE_OUT'''
		return self._instance.FileOut

	@property
	def file_name(self) -> str:
		'''Value of variable $FILE_NAME'''
		return self._instance.FileName

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SyslogSavVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
