import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DeflogicVariableType as deflogic_variable_type

class DeflogicVariableType(GenericVariableType):
	'''Describes the Fanuc type DEFLOGIC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = deflogic_variable_type()
		else:
			self._instance = _internal

	@property
	def func_title(self) -> str:
		'''Value of variable $FUNC_TITLE'''
		return self._instance.FuncTitle

	@property
	def total_num(self) -> int:
		'''Value of variable $TOTAL_NUM'''
		return self._instance.TotalNum

	@property
	def dummy2(self) -> int:
		'''Value of variable $DUMMY2'''
		return self._instance.Dummy2

	@property
	def dummy3(self) -> int:
		'''Value of variable $DUMMY3'''
		return self._instance.Dummy3

	@property
	def dummy4(self) -> int:
		'''Value of variable $DUMMY4'''
		return self._instance.Dummy4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DeflogicVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
