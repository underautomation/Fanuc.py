import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.variables.generic_variable import GenericVariable
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableFile as generic_variable_file

class GenericVariableFile(IGenericVariableType, IFanucContent):
	'''Represents a parsed Fanuc variable file containing one or more variables'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_file()
		else:
			self._instance = _internal

	def get_field(self, name: str) -> GenericVariable:
		'''Gets a variable by name (case-insensitive)'''
		return GenericVariable(self._instance.GetField(name))

	def generate_va(self, stream: typing.Any) -> None:
		'''Generates a .va file and writes it to the specified stream'''
		self._instance.GenerateVa(stream)

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def generated_va(self) -> str:
		return self._instance.GeneratedVa()

	@property
	def variables(self) -> typing.List[GenericVariable]:
		'''Variables declared in this file'''
		return [GenericVariable(x) for x in self._instance.Variables]

	@property
	def name(self) -> str:
		'''File name'''
		return self._instance.Name

	@property
	def parent(self) -> IGenericVariableType:
		'''Parent container'''
		return IGenericVariableType(self._instance.Parent)

	@parent.setter
	def parent(self, value: IGenericVariableType):
		self._instance.Parent = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GenericVariableFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
