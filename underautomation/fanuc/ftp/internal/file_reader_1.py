import typing
from underautomation.fanuc.ftp.internal.i_file_reader_1 import IFileReader1
from underautomation.fanuc.ftp.internal.i_file_reader import IFileReader
from underautomation.fanuc.ftp.internal.file_reader import FileReader
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FileReader as file_reader_1

T = typing.TypeVar('T')
class FileReader1(FileReader, IFileReader1[T], IFileReader, typing.Generic[T]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_reader_1()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str="None") -> T:
		return self._instance.ReadFile(fileStream, fileName)
