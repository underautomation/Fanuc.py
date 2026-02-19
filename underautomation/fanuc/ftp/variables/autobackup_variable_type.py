import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AutobackupVariableType as autobackup_variable_type

class AutobackupVariableType(GenericVariableType):
	'''Describes the Fanuc type AUTOBACKUP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = autobackup_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def device(self) -> str:
		'''Value of variable $DEVICE'''
		return self._instance.Device

	@property
	def time(self) -> typing.List[int]:
		'''Value of variable $TIME'''
		return self._instance.Time

	@property
	def di_idx(self) -> int:
		'''Value of variable $DI_IDX'''
		return self._instance.DiIdx

	@property
	def startup_bck(self) -> bool:
		'''Value of variable $STARTUP_BCK'''
		return self._instance.StartupBck

	@property
	def interval(self) -> int:
		'''Value of variable $INTERVAL'''
		return self._instance.Interval

	@property
	def disp_unit(self) -> int:
		'''Value of variable $DISP_UNIT'''
		return self._instance.DispUnit

	@property
	def bck_do_idx(self) -> int:
		'''Value of variable $BCK_DO_IDX'''
		return self._instance.BckDoIdx

	@property
	def err_do_idx(self) -> int:
		'''Value of variable $ERR_DO_IDX'''
		return self._instance.ErrDoIdx

	@property
	def fr_free(self) -> int:
		'''Value of variable $FR_FREE'''
		return self._instance.FrFree

	@property
	def in_progress(self) -> int:
		'''Value of variable $IN_PROGRESS'''
		return self._instance.InProgress

	@property
	def req_backup(self) -> int:
		'''Value of variable $REQ_BACKUP'''
		return self._instance.ReqBackup

	@property
	def prc_wait(self) -> int:
		'''Value of variable $PRC_WAIT'''
		return self._instance.PrcWait

	@property
	def auto_backup(self) -> int:
		'''Value of variable $AUTO_BACKUP'''
		return self._instance.AutoBackup

	@property
	def poff_count(self) -> int:
		'''Value of variable $POFF_COUNT'''
		return self._instance.PoffCount

	@property
	def del_count(self) -> int:
		'''Value of variable $DEL_COUNT'''
		return self._instance.DelCount

	@property
	def log_idx(self) -> int:
		'''Value of variable $LOG_IDX'''
		return self._instance.LogIdx

	@property
	def del_time(self) -> typing.List[str]:
		'''Value of variable $DEL_TIME'''
		return self._instance.DelTime

	@property
	def del_file(self) -> typing.List[str]:
		'''Value of variable $DEL_FILE'''
		return self._instance.DelFile

	@property
	def proc_file(self) -> str:
		'''Value of variable $PROC_FILE'''
		return self._instance.ProcFile

	@property
	def last_time(self) -> int:
		'''Value of variable $LAST_TIME'''
		return self._instance.LastTime

	@property
	def atb_count(self) -> int:
		'''Value of variable $ATB_COUNT'''
		return self._instance.AtbCount

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AutobackupVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
