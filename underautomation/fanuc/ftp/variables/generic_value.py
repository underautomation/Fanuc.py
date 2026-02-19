import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.value_kind import ValueKind
# Circular dependencies  : GenericField
from UnderAutomation.Fanuc.Ftp.Variables import GenericValue as generic_value
from UnderAutomation.Fanuc.Ftp.Variables import ValueKind as value_kind

class GenericValue(IGenericVariableType):
	'''Represents a generic variable value with optional child fields'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_value()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def parent(self) -> 'GenericValue':
		'''Parent value that contains this value'''
		return GenericValue(self._instance.Parent)

	@property
	def kind(self) -> ValueKind:
		'''Kind of value (scalar, array, structure, or file)'''
		return ValueKind(int(self._instance.Kind))

	@property
	def fields(self) -> typing.Any:
		'''Child fields of this value'''
		from underautomation.fanuc.ftp.variables.generic_field import GenericField
		return [GenericField(x) for x in self._instance.Fields]

	@property
	def name(self) -> str:
		'''Name of this value'''
		return self._instance.Name

	@property
	def is_uninitialized(self) -> bool:
		'''Indicates whether this value is uninitialized'''
		return self._instance.IsUninitialized

	@property
	def value(self) -> str:
		'''String representation of the value'''
		return self._instance.Value

	@property
	def register_name(self) -> str:
		'''Register name associated with this value'''
		return self._instance.RegisterName

	@property
	def full_name(self) -> str:
		'''Fully qualified name including all parent names'''
		return self._instance.FullName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
