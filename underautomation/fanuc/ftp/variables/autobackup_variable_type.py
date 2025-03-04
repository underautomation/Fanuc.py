import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AutobackupVariableType as autobackup_variable_type

class AutobackupVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = autobackup_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def device(self) -> str:
		return self._instance.Device
	@property
	def time(self) -> typing.List[int]:
		return self._instance.Time
	@property
	def di_idx(self) -> int:
		return self._instance.DiIdx
	@property
	def startup_bck(self) -> bool:
		return self._instance.StartupBck
	@property
	def interval(self) -> int:
		return self._instance.Interval
	@property
	def disp_unit(self) -> int:
		return self._instance.DispUnit
	@property
	def bck_do_idx(self) -> int:
		return self._instance.BckDoIdx
	@property
	def err_do_idx(self) -> int:
		return self._instance.ErrDoIdx
	@property
	def fr_free(self) -> int:
		return self._instance.FrFree
	@property
	def in_progress(self) -> int:
		return self._instance.InProgress
	@property
	def req_backup(self) -> int:
		return self._instance.ReqBackup
	@property
	def prc_wait(self) -> int:
		return self._instance.PrcWait
	@property
	def auto_backup(self) -> int:
		return self._instance.AutoBackup
	@property
	def poff_count(self) -> int:
		return self._instance.PoffCount
	@property
	def del_count(self) -> int:
		return self._instance.DelCount
	@property
	def log_idx(self) -> int:
		return self._instance.LogIdx
	@property
	def del_time(self) -> typing.List[str]:
		return self._instance.DelTime
	@property
	def del_file(self) -> typing.List[str]:
		return self._instance.DelFile
	@property
	def proc_file(self) -> str:
		return self._instance.ProcFile
	@property
	def last_time(self) -> int:
		return self._instance.LastTime
	@property
	def atb_count(self) -> int:
		return self._instance.AtbCount
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
