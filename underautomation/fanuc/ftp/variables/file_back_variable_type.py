import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FileBackVariableType as file_back_variable_type

class FileBackVariableType(GenericVariableType):
	'''Describes the Fanuc type FILE_BACK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_back_variable_type()
		else:
			self._instance = _internal

	@property
	def file_name(self) -> str:
		'''Value of variable $FILE_NAME'''
		return self._instance.FileName

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def func_code(self) -> int:
		'''Value of variable $FUNC_CODE'''
		return self._instance.FuncCode

	@property
	def modifier(self) -> int:
		'''Value of variable $MODIFIER'''
		return self._instance.Modifier

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def func_ptr(self) -> int:
		'''Value of variable $FUNC_PTR'''
		return self._instance.FuncPtr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileBackVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
