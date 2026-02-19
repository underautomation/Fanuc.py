import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FtpCtrlVariableType as ftp_ctrl_variable_type

class FtpCtrlVariableType(GenericVariableType):
	'''Describes the Fanuc type FTP_CTRL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_ctrl_variable_type()
		else:
			self._instance = _internal

	@property
	def log_entries(self) -> int:
		'''Value of variable $LOG_ENTRIES'''
		return self._instance.LogEntries

	@property
	def log_cmos(self) -> bool:
		'''Value of variable $LOG_CMOS'''
		return self._instance.LogCmos

	@property
	def dnld_filter(self) -> bool:
		'''Value of variable $DNLD_FILTER'''
		return self._instance.DnldFilter

	@property
	def subdircaps(self) -> bool:
		'''Value of variable $SUBDIRCAPS'''
		return self._instance.Subdircaps

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpCtrlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
