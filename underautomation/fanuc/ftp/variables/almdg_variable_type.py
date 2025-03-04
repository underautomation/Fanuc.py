import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AlmdgVariableType as almdg_variable_type

class AlmdgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = almdg_variable_type()
		else:
			self._instance = _internal
	@property
	def debug1(self) -> int:
		return self._instance.Debug1
	@property
	def debug2(self) -> int:
		return self._instance.Debug2
	@property
	def debug3(self) -> int:
		return self._instance.Debug3
	@property
	def cont_type(self) -> int:
		return self._instance.ContType
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
