import typing
from UnderAutomation.Fanuc.Ftp.Variables import IGenericVariableType as i_generic_variable_type

class IGenericVariableType:
	'''Interface for a structure that contains variables'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_generic_variable_type()
		else:
			self._instance = _internal

	@property
	def fields(self) -> typing.List['IGenericVariableType']:
		'''Fields inside this structure'''
		return [IGenericVariableType(x) for x in self._instance.Fields]

	@property
	def name(self) -> str:
		'''Name of the structure'''
		return self._instance.Name

	@property
	def parent(self) -> 'IGenericVariableType':
		'''Parent of this structure'''
		return IGenericVariableType(self._instance.Parent)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IGenericVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
