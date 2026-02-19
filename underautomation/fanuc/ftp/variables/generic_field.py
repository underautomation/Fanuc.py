import typing
# Circular dependencies  : GenericValue
from underautomation.fanuc.ftp.variables.generic_value import GenericValue
from UnderAutomation.Fanuc.Ftp.Variables import GenericField as generic_field

class GenericField(GenericValue):
	'''Represents a named field within a variable structure'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_field()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def access(self) -> str:
		'''Access modifier of the field (e.g. RW, RO)'''
		return self._instance.Access

	@property
	def type(self) -> str:
		'''Data type name of the field'''
		return self._instance.Type

	@type.setter
	def type(self, value: str):
		self._instance.Type = value

	@property
	def is_register(self) -> bool:
		'''Indicates whether this field is a register'''
		return self._instance.IsRegister

	@property
	def string_length(self) -> int:
		'''Maximum string length if the field type is STRING'''
		return self._instance.StringLength

	@property
	def dimension1(self) -> int:
		'''First dimension size of the array, or first index of an array element'''
		return self._instance.Dimension1

	@property
	def dimension2(self) -> int:
		'''Second dimension size of the array, or second index of an array element'''
		return self._instance.Dimension2

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericField):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
