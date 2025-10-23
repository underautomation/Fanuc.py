import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.generic_field import GenericField
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableType as generic_variable_type

class GenericVariableType(IGenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_type()
		else:
			self._instance = _internal
	def get_field(self, name: str) -> GenericField:
		return GenericField(self._instance.GetField(name))
	@property
	def fields(self) -> typing.List[GenericField]:
		return [GenericField(x) for x in self._instance.Fields]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
	@property
	def parent(self) -> IGenericVariableType:
		return IGenericVariableType(self._instance.Parent)
