import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HttpAuthVariableType as http_auth_variable_type

class HttpAuthVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_auth_variable_type()
		else:
			self._instance = _internal
	@property
	def object(self) -> str:
		return self._instance.Object
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def level(self) -> int:
		return self._instance.Level
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
