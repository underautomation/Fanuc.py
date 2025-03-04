import typing
from underautomation.fanuc.ftp.diagnosis.summary_diagnosis import SummaryDiagnosis
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import SummaryDiagnosisReader as summary_diagnosis_reader

class SummaryDiagnosisReader(FileReader1[SummaryDiagnosis]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = summary_diagnosis_reader()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str) -> SummaryDiagnosis:
		return SummaryDiagnosis(self._instance.ReadFile(fileStream, fileName))
