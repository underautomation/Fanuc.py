import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ShellChkVariableType as shell_chk_variable_type

class ShellChkVariableType(GenericVariableType):
	'''Describes the Fanuc type SHELL_CHK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_chk_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def resume(self) -> bool:
		'''Value of variable $RESUME'''
		return self._instance.Resume

	@property
	def prompt(self) -> bool:
		'''Value of variable $PROMPT'''
		return self._instance.Prompt

	@property
	def errpost(self) -> bool:
		'''Value of variable $ERRPOST'''
		return self._instance.Errpost

	@property
	def force(self) -> bool:
		'''Value of variable $FORCE'''
		return self._instance.Force

	@property
	def warn(self) -> bool:
		'''Value of variable $WARN'''
		return self._instance.Warn

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellChkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
