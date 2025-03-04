import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IoslaveVariableType as ioslave_variable_type

class IoslaveVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ioslave_variable_type()
		else:
			self._instance = _internal
	@property
	def input_n(self) -> int:
		return self._instance.InputN
	@property
	def output_n(self) -> int:
		return self._instance.OutputN
	@property
	def input_n2(self) -> int:
		return self._instance.InputN2
	@property
	def output_n2(self) -> int:
		return self._instance.OutputN2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
