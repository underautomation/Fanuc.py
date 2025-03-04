import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FluiDataVariableType as flui_data_variable_type

class FluiDataVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_data_variable_type()
		else:
			self._instance = _internal
	@property
	def future1(self) -> int:
		return self._instance.Future1
	@property
	def future2(self) -> int:
		return self._instance.Future2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
