import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.i_file_reader_1 import IFileReader1
from underautomation.fanuc.ftp.variables.variable_reader import VariableReader
from underautomation.fanuc.ftp.list.error_list_reader import ErrorListReader
from underautomation.fanuc.ftp.diagnosis.summary_diagnosis_reader import SummaryDiagnosisReader
from underautomation.fanuc.ftp.diagnosis.diagnosis_reader_2 import DiagnosisReader2
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.ftp.diagnosis.current_position_reader import CurrentPositionReader
from underautomation.fanuc.ftp.diagnosis.io_state import IOState
from underautomation.fanuc.ftp.diagnosis.io_state_parser import IOStateParser
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.ftp.diagnosis.safety_status_parser import SafetyStatusParser
from underautomation.fanuc.ftp.diagnosis.program_states import ProgramStates
from underautomation.fanuc.ftp.diagnosis.program_states_parser import ProgramStatesParser
from UnderAutomation.Fanuc.Ftp import FanucFileReaders as fanuc_file_readers
from UnderAutomation.Fanuc.Common import Languages as languages

class FanucFileReaders:
	'''Contains static functions to decode Fanuc files (variables, diagnosis, listing, ...)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fanuc_file_readers()
		else:
			self._instance = _internal

	@staticmethod
	def read_file(fileStream: typing.Any, fileName: str, language: Languages) -> IFanucContent:
		'''Read any file by path on disc, recognize it by name and decode it'''
		return IFanucContent(fanuc_file_readers.ReadFile(fileStream, fileName, languages(int(language))))

	@property
	def readers(self) -> typing.List[IFileReader1]:
		'''Get the collection of all parsers'''
		return [IFileReader1(x) for x in self._instance.Readers]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FanucFileReaders):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Helper to read variable files *.va
FanucFileReaders.VariableReader = VariableReader(fanuc_file_readers.VariableReader)

# Helper to read error files like errall.ls
FanucFileReaders.ErrorListReader = ErrorListReader(fanuc_file_readers.ErrorListReader)

# Helper to read summary diagnosis file summary.dg
FanucFileReaders.SummaryDiagnosticReader = SummaryDiagnosisReader(fanuc_file_readers.SummaryDiagnosticReader)

# Decode current position file curpos.dg
FanucFileReaders.CurrentPositionReader = DiagnosisReader2[CurrentPosition, CurrentPositionReader](fanuc_file_readers.CurrentPositionReader)

# Decode IO Status file iostate.dg
FanucFileReaders.IOStateReader = DiagnosisReader2[IOState, IOStateParser](fanuc_file_readers.IOStateReader)

# Decode IO Status file iostate.dg
FanucFileReaders.SafetyStatusReader = DiagnosisReader2[SafetyStatus, SafetyStatusParser](fanuc_file_readers.SafetyStatusReader)

# Decode task and program states prgstate.dg
FanucFileReaders.ProgramStates = DiagnosisReader2[ProgramStates, ProgramStatesParser](fanuc_file_readers.ProgramStates)
