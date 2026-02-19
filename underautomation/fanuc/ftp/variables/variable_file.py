import typing
from UnderAutomation.Fanuc.Ftp.Variables import VariableFile as variable_file

class VariableFile:
	'''Abstract base class for typed variable file readers'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_file()
		else:
			self._instance = _internal

	@property
	def file_name(self) -> str:
		'''Name of the variable file'''
		return self._instance.FileName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VariableFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
