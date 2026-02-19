import typing
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
from UnderAutomation.Fanuc.Ftp.Variables import VariableReader as variable_reader_1
from UnderAutomation.Fanuc.Common import Languages as languages

T = typing.TypeVar('T')
class VariableReader1(FileReader1[T], typing.Generic[T]):
	'''Typed variable file reader for specific variable file types'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_reader_1()
		else:
			self._instance = _internal

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str) -> T:
		return self._instance.ReadFile(fileStream, languages(int(language)), fileName)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VariableReader1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
