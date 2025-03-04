import typing
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import DiagnosisReader as diagnosis_reader_2

T = typing.TypeVar('T')
U = typing.TypeVar('U')
class DiagnosisReader2(FileReader1[T], typing.Generic[T, U]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = diagnosis_reader_2()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str="None") -> T:
		return self._instance.ReadFile(fileStream, fileName)
