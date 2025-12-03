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

FanucFileReaders.variable_reader = FanucFileReaders(fanuc_file_readers.VariableReader)

FanucFileReaders.error_list_reader = FanucFileReaders(fanuc_file_readers.ErrorListReader)

FanucFileReaders.summary_diagnostic_reader = FanucFileReaders(fanuc_file_readers.SummaryDiagnosticReader)

FanucFileReaders.current_position_reader = FanucFileReaders(fanuc_file_readers.CurrentPositionReader)

FanucFileReaders.io_state_reader = FanucFileReaders(fanuc_file_readers.IOStateReader)

FanucFileReaders.safety_status_reader = FanucFileReaders(fanuc_file_readers.SafetyStatusReader)

FanucFileReaders.program_states = FanucFileReaders(fanuc_file_readers.ProgramStates)
