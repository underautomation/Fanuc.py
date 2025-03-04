import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FtpCtrlVariableType as ftp_ctrl_variable_type

class FtpCtrlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_ctrl_variable_type()
		else:
			self._instance = _internal
	@property
	def log_entries(self) -> int:
		return self._instance.LogEntries
	@property
	def log_cmos(self) -> bool:
		return self._instance.LogCmos
	@property
	def dnld_filter(self) -> bool:
		return self._instance.DnldFilter
	@property
	def subdircaps(self) -> bool:
		return self._instance.Subdircaps
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
