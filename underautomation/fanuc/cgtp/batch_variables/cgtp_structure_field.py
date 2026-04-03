from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpStructureField as cgtp_structure_field

class CgtpStructureField:
	'''Represents a FIELD or ARRAY node inside a structured variable response.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_structure_field()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Field or array element name'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def string_value(self) -> str:
		'''Text content of this node. Null if this node has children.'''
		return self._instance.StringValue

	@string_value.setter
	def string_value(self, value: str):
		self._instance.StringValue = value

	@property
	def is_read_only(self) -> bool:
		'''Whether this node is read-only on the controller'''
		return self._instance.IsReadOnly

	@is_read_only.setter
	def is_read_only(self, value: bool):
		self._instance.IsReadOnly = value

	@property
	def is_array(self) -> bool:
		'''True if this node was an ARRAY element, false if it was a FIELD'''
		return self._instance.IsArray

	@is_array.setter
	def is_array(self, value: bool):
		self._instance.IsArray = value

	@property
	def children(self) -> typing.List['CgtpStructureField']:
		'''Child nodes (FIELD and ARRAY elements). Null if this is a leaf node.'''
		return [CgtpStructureField(x) for x in self._instance.Children]

	@children.setter
	def children(self, value: typing.List['CgtpStructureField']):
		self._instance.Children = [x._instance if x else None for x in value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpStructureField):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
