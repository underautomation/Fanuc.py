import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ShellCommVariableType as shell_comm_variable_type

class ShellCommVariableType(GenericVariableType):
	'''Describes the Fanuc type SHELL_COMM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = shell_comm_variable_type()
		else:
			self._instance = _internal

	@property
	def func(self) -> int:
		'''Value of variable $FUNC'''
		return self._instance.Func

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def parm1(self) -> int:
		'''Value of variable $PARM1'''
		return self._instance.Parm1

	@property
	def parm2(self) -> int:
		'''Value of variable $PARM2'''
		return self._instance.Parm2

	@property
	def parm3(self) -> int:
		'''Value of variable $PARM3'''
		return self._instance.Parm3

	@property
	def parm4(self) -> int:
		'''Value of variable $PARM4'''
		return self._instance.Parm4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ShellCommVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
