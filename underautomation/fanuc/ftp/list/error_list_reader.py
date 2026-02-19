import typing
from underautomation.fanuc.ftp.list.error_list import ErrorList
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
from UnderAutomation.Fanuc.Ftp.List import ErrorListReader as error_list_reader
from UnderAutomation.Fanuc.Common import Languages as languages

class ErrorListReader(FileReader1[ErrorList]):
	'''Reader for the ERRALL.LS error log file'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the error list reader'''
		if(_internal == 0):
			self._instance = error_list_reader()
		else:
			self._instance = _internal

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str="None") -> ErrorList:
		return ErrorList(self._instance.ReadFile(fileStream, languages(int(language)), fileName))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErrorListReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
