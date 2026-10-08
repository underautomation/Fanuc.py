from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common.Files.Variables import IGenericVariableType as i_generic_variable_type

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
		__r = self._instance.Fields
		return None if __r is None else [None if x is None else IGenericVariableType(x) for x in __r]

	@property
	def name(self) -> str:
		'''Name of the structure'''
		return self._instance.Name

	@property
	def parent(self) -> 'IGenericVariableType':
		'''Parent of this structure'''
		__r = self._instance.Parent
		return None if __r is None else IGenericVariableType(__r)

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
