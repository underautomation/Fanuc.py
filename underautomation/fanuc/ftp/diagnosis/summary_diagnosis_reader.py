import typing
from underautomation.fanuc.ftp.diagnosis.summary_diagnosis import SummaryDiagnosis
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
from UnderAutomation.Fanuc.Ftp.Diagnosis import SummaryDiagnosisReader as summary_diagnosis_reader
from UnderAutomation.Fanuc.Common import Languages as languages

class SummaryDiagnosisReader(FileReader1[SummaryDiagnosis]):
	'''Read and parse the file summary.dg'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = summary_diagnosis_reader()
		else:
			self._instance = _internal

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str) -> SummaryDiagnosis:
		'''Read and parse the file'''
		return SummaryDiagnosis(self._instance.ReadFile(fileStream, languages(int(language)), fileName))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SummaryDiagnosisReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
