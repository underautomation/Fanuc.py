import typing
from underautomation.fanuc.ftp.list.error_list import ErrorList
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.List import ErrorListReader as error_list_reader

class ErrorListReader(FileReader1[ErrorList]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = error_list_reader()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str="None") -> ErrorList:
		return ErrorList(self._instance.ReadFile(fileStream, fileName))
