import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.generic_field import GenericField
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariable as generic_variable

class GenericVariable(GenericField, IGenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable()
		else:
			self._instance = _internal
	@property
	def scope(self) -> str:
		return self._instance.Scope
	@property
	def storage(self) -> str:
		return self._instance.Storage
	@property
	def parent(self) -> IGenericVariableType:
		return IGenericVariableType(self._instance.Parent)
