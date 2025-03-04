import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DetIoVariableType as det_io_variable_type

class DetIoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = det_io_variable_type()
		else:
			self._instance = _internal
	@property
	def io_type(self) -> int:
		return self._instance.IoType
	@property
	def io_port(self) -> int:
		return self._instance.IoPort
	@property
	def style(self) -> int:
		return self._instance.Style
	@property
	def limit(self) -> int:
		return self._instance.Limit
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
