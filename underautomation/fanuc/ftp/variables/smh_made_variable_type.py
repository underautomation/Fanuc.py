import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SmhMadeVariableType as smh_made_variable_type

class SmhMadeVariableType(GenericVariableType):
	'''Describes the Fanuc type SMH_MADE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smh_made_variable_type()
		else:
			self._instance = _internal

	@property
	def made_tasks(self) -> int:
		'''Value of variable $MADE_TASKS'''
		return self._instance.MadeTasks

	@property
	def made_grups(self) -> int:
		'''Value of variable $MADE_GRUPS'''
		return self._instance.MadeGrups

	@property
	def made_mirs(self) -> int:
		'''Value of variable $MADE_MIRS'''
		return self._instance.MadeMirs

	@property
	def made_amrs(self) -> int:
		'''Value of variable $MADE_AMRS'''
		return self._instance.MadeAmrs

	@property
	def made_mode(self) -> int:
		'''Value of variable $MADE_MODE'''
		return self._instance.MadeMode

	@property
	def made_stk(self) -> int:
		'''Value of variable $MADE_STK'''
		return self._instance.MadeStk

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SmhMadeVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
