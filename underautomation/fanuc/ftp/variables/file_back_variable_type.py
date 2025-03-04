import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FileBackVariableType as file_back_variable_type

class FileBackVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_back_variable_type()
		else:
			self._instance = _internal
	@property
	def file_name(self) -> str:
		return self._instance.FileName
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def func_code(self) -> int:
		return self._instance.FuncCode
	@property
	def modifier(self) -> int:
		return self._instance.Modifier
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def func_ptr(self) -> int:
		return self._instance.FuncPtr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
