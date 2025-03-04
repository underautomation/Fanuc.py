import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Sbr2VariableType as sbr2_variable_type

class Sbr2VariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sbr2_variable_type()
		else:
			self._instance = _internal
	@property
	def param(self) -> typing.List[int]:
		return self._instance.Param
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
