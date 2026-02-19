import typing
from underautomation.fanuc.ftp.internal.i_file_reader_1 import IFileReader1
from underautomation.fanuc.ftp.internal.i_file_reader import IFileReader
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.file_reader import FileReader
from UnderAutomation.Fanuc.Ftp.Internal import FileReader as file_reader_1
from UnderAutomation.Fanuc.Common import Languages as languages

T = typing.TypeVar('T')
class FileReader1(FileReader, IFileReader1[T], IFileReader, typing.Generic[T]):
	'''File reader for specific files'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_reader_1()
		else:
			self._instance = _internal

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str="None") -> T:
		'''Read and decode the file stream'''
		return self._instance.ReadFile(fileStream, languages(int(language)), fileName)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileReader1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
