import typing
from underautomation.fanuc.ftp.internal.i_file_reader import IFileReader
from underautomation.fanuc.common.languages import Languages
from UnderAutomation.Fanuc.Ftp.Internal import IFileReader as i_file_reader_1
from UnderAutomation.Fanuc.Common import Languages as languages

T = typing.TypeVar('T')
class IFileReader1(IFileReader, typing.Generic[T]):
	'''Interface for Fanuc file readers'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_reader_1()
		else:
			self._instance = _internal

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str) -> T:
		'''Reads file stream and decodes it'''
		return self._instance.ReadFile(fileStream, languages(int(language)), fileName)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IFileReader1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
