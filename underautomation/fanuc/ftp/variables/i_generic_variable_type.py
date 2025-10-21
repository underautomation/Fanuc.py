import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IGenericVariableType as i_generic_variable_type

class IGenericVariableType:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_generic_variable_type()
		else:
			self._instance = _internal
	@property
	def fields(self) -> typing.List['IGenericVariableType']:
		return [IGenericVariableType(x) for x in self._instance.Fields]
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def parent(self) -> 'IGenericVariableType':
		return IGenericVariableType(self._instance.Parent)
