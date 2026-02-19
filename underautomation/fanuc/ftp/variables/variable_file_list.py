import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import VariableFileList as variable_file_list

class VariableFileList(IGenericVariableType):
	'''Collection of variable files that aggregates all variables from the controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_file_list()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of this variable file list'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

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
		if not isinstance(other, VariableFileList):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __iter__(self):
		enumerator = self._instance.GetEnumerator()
		while enumerator.MoveNext():
			yield enumerator.Current

	def __len__(self) -> int:
		return self._instance.Count

	def __getitem__(self, index: int) -> T:
		return self._instance[index]
