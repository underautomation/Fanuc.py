import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.generic_field import GenericField
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableType as generic_variable_type

class GenericVariableType(IGenericVariableType):
	'''Abstract base class for typed variable structures'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_type()
		else:
			self._instance = _internal

	def get_field(self, name: str) -> GenericField:
		'''Gets a field by name (case-insensitive)'''
		return GenericField(self._instance.GetField(name))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def fields(self) -> typing.List[GenericField]:
		'''Fields contained in this type'''
		return [GenericField(x) for x in self._instance.Fields]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Internal Fanuc type name'''
		return self._instance.FanucInternalTypeName

	@property
	def parent(self) -> IGenericVariableType:
		'''Parent container'''
		return IGenericVariableType(self._instance.Parent)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
