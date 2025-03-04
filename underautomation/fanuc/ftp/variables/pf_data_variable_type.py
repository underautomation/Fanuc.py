import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PfDataVariableType as pf_data_variable_type

class PfDataVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_data_variable_type()
		else:
			self._instance = _internal
	@property
	def value(self) -> float:
		return self._instance.Value
	@property
	def group(self) -> int:
		return self._instance.Group
	@property
	def axis(self) -> int:
		return self._instance.Axis
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
