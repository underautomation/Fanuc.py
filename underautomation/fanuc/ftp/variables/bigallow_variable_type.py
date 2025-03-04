import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import BigallowVariableType as bigallow_variable_type

class BigallowVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bigallow_variable_type()
		else:
			self._instance = _internal
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def var_name(self) -> str:
		return self._instance.VarName
	@property
	def index(self) -> int:
		return self._instance.Index
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
