import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpTestVariableType as cp_test_variable_type

class CpTestVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_test_variable_type()
		else:
			self._instance = _internal
	@property
	def enable_test(self) -> bool:
		return self._instance.EnableTest
	@property
	def num_lines(self) -> int:
		return self._instance.NumLines
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
