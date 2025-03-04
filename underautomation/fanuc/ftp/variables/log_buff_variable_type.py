import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LogBuffVariableType as log_buff_variable_type

class LogBuffVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_buff_variable_type()
		else:
			self._instance = _internal
	@property
	def title(self) -> str:
		return self._instance.Title
	@property
	def size(self) -> int:
		return self._instance.Size
	@property
	def mem_type(self) -> int:
		return self._instance.MemType
	@property
	def visible(self) -> bool:
		return self._instance.Visible
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
