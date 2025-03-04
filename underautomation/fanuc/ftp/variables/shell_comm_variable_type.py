import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ShellCommVariableType as shell_comm_variable_type

class ShellCommVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_comm_variable_type()
		else:
			self._instance = _internal
	@property
	def func(self) -> int:
		return self._instance.Func
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def parm1(self) -> int:
		return self._instance.Parm1
	@property
	def parm2(self) -> int:
		return self._instance.Parm2
	@property
	def parm3(self) -> int:
		return self._instance.Parm3
	@property
	def parm4(self) -> int:
		return self._instance.Parm4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
