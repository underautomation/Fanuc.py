import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableTypeHelpers as generic_variable_type_helpers

class GenericVariableTypeHelpers:
	'''Extension methods for IGenericVariableType'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_type_helpers()
		else:
			self._instance = _internal

	@staticmethod
	def get_ancestors(element: IGenericVariableType) -> typing.List[IGenericVariableType]:
		'''Recursively get parents in an array. The first element is the root element and the last one is the direct parent of the element.'''
		return [IGenericVariableType(x) for x in generic_variable_type_helpers.GetAncestors(element._instance if element else None)]

	@staticmethod
	def get_field(element: IGenericVariableType, name: str) -> IGenericVariableType:
		'''Get a field by its name (case insensitive)'''
		return IGenericVariableType(generic_variable_type_helpers.GetField(element._instance if element else None, name))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericVariableTypeHelpers):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
