import typing
from underautomation.fanuc.ftp.internal.i_file_reader import IFileReader
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import IFileReader as i_file_reader_1

T = typing.TypeVar('T')
class IFileReader1(IFileReader, typing.Generic[T]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_reader_1()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str) -> T:
		return self._instance.ReadFile(fileStream, fileName)
