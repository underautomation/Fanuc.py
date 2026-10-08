from __future__ import annotations
import typing
from underautomation.fanuc.common.files.i_file_reader_1 import IFileReader1
from underautomation.fanuc.common.files.i_file_reader import IFileReader
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.common.files.file_reader import FileReader
from UnderAutomation.Fanuc.Common.Files import FileReader as file_reader_1
from UnderAutomation.Fanuc.Common import Languages as languages

T = typing.TypeVar('T')
class FileReader1(FileReader, IFileReader1[T], typing.Generic[T]):
	'''File reader for specific files'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_reader_1()
		else:
			self._instance = _internal

	def read_file(self, filePath: str, language: Languages) -> T:
		'''Read and decode the file on disc'''
		return self._instance.ReadFile(filePath, languages(int(language)))

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
