import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DeflogicVariableType as deflogic_variable_type

class DeflogicVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = deflogic_variable_type()
		else:
			self._instance = _internal
	@property
	def func_title(self) -> str:
		return self._instance.FuncTitle
	@property
	def total_num(self) -> int:
		return self._instance.TotalNum
	@property
	def dummy2(self) -> int:
		return self._instance.Dummy2
	@property
	def dummy3(self) -> int:
		return self._instance.Dummy3
	@property
	def dummy4(self) -> int:
		return self._instance.Dummy4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
