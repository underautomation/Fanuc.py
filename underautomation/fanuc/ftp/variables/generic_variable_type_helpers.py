import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableTypeHelpers as generic_variable_type_helpers

class GenericVariableTypeHelpers:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_type_helpers()
		else:
			self._instance = _internal
	@staticmethod
	def get_ancestors(element: IGenericVariableType) -> typing.List[IGenericVariableType]:
		return [IGenericVariableType(x) for x in generic_variable_type_helpers.GetAncestors(element._instance if element else None)]
	@staticmethod
	def get_field(element: IGenericVariableType, name: str) -> IGenericVariableType:
		return IGenericVariableType(generic_variable_type_helpers.GetField(element._instance if element else None, name))
