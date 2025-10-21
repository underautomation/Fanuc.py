import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import IFileReader as i_file_reader

class IFileReader:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_file_reader()
		else:
			self._instance = _internal
	@property
	def file_name(self) -> str:
		return self._instance.FileName
