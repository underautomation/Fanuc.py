import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.generic_field import GenericField
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariable as generic_variable

class GenericVariable(GenericField, IGenericVariableType):
	'''Represents a top-level variable declaration with scope and storage information'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def scope(self) -> str:
		'''Variable scope (e.g. PROG, SYS)'''
		return self._instance.Scope

	@property
	def storage(self) -> str:
		'''Storage type of the variable (e.g. CMOS, DRAM)'''
		return self._instance.Storage

	@property
	def parent(self) -> IGenericVariableType:
		'''Parent container of this variable'''
		return IGenericVariableType(self._instance.Parent)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
