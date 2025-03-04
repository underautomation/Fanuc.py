import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VrtdFiltVariableType as vrtd_filt_variable_type

class VrtdFiltVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vrtd_filt_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def dummy4(self) -> int:
		return self._instance.Dummy4
	@property
	def tool_type(self) -> int:
		return self._instance.ToolType
	@property
	def words(self) -> str:
		return self._instance.Words
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
