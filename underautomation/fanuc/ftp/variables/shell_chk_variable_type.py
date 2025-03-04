import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ShellChkVariableType as shell_chk_variable_type

class ShellChkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_chk_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def resume(self) -> bool:
		return self._instance.Resume
	@property
	def prompt(self) -> bool:
		return self._instance.Prompt
	@property
	def errpost(self) -> bool:
		return self._instance.Errpost
	@property
	def force(self) -> bool:
		return self._instance.Force
	@property
	def warn(self) -> bool:
		return self._instance.Warn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
