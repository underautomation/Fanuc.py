import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
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
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp import FanucFileReaders as fanuc_file_readers

class FanucFileReaders:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fanuc_file_readers()
		else:
			self._instance = _internal
	@staticmethod
	def read_file(fileStream: typing.Any, fileName: str) -> IFanucContent:
		return IFanucContent(fanuc_file_readers.ReadFile(fileStream, fileName))
	@property
	def readers(self) -> typing.List[IFileReader1]:
		return [IFileReader1(x) for x in self._instance.Readers]
	@property
	def variable_reader(self) -> VariableReader:
		return VariableReader(self._instance.VariableReader)
	@property
	def error_list_reader(self) -> ErrorListReader:
		return ErrorListReader(self._instance.ErrorListReader)
	@property
	def summary_diagnostic_reader(self) -> SummaryDiagnosisReader:
		return SummaryDiagnosisReader(self._instance.SummaryDiagnosticReader)
	@property
	def current_position_reader(self) -> DiagnosisReader2[CurrentPosition, CurrentPositionReader]:
		return DiagnosisReader2[CurrentPosition, CurrentPositionReader](self._instance.CurrentPositionReader)
	@property
	def io_state_reader(self) -> DiagnosisReader2[IOState, IOStateParser]:
		return DiagnosisReader2[IOState, IOStateParser](self._instance.IOStateReader)
	@property
	def safety_status_reader(self) -> DiagnosisReader2[SafetyStatus, SafetyStatusParser]:
		return DiagnosisReader2[SafetyStatus, SafetyStatusParser](self._instance.SafetyStatusReader)
	@property
	def program_states(self) -> DiagnosisReader2[ProgramStates, ProgramStatesParser]:
		return DiagnosisReader2[ProgramStates, ProgramStatesParser](self._instance.ProgramStates)
