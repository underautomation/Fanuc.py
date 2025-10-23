import typing
from underautomation.fanuc.ftp.internal.i_file_reader import IFileReader
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FileReader as file_reader

class FileReader(IFileReader):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_reader()
		else:
			self._instance = _internal
	@property
	def file_name(self) -> str:
		return self._instance.FileName
