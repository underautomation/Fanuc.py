import typing
from underautomation.fanuc.ftp.internal.ftp_direct_file_handling import FtpDirectFileHandling
from underautomation.fanuc.ftp.internal.ftp_known_variable_files import FtpKnownVariableFiles
from underautomation.fanuc.ftp.diagnosis.summary_diagnosis import SummaryDiagnosis
from underautomation.fanuc.ftp.list.error_list import ErrorList
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.ftp.diagnosis.io_state import IOState
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.ftp.diagnosis.program_states import ProgramStates
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from underautomation.fanuc.ftp.ftp_list_item import FtpListItem
from underautomation.fanuc.ftp.variables.variable_file_list import VariableFileList
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FtpClientBase as ftp_client_base

class FtpClientBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_base()
		else:
			self._instance = _internal
	def disconnect(self) -> None:
		self._instance.Disconnect()
	def get_summary_diagnostic(self) -> SummaryDiagnosis:
		return SummaryDiagnosis(self._instance.GetSummaryDiagnostic())
	def get_all_errors_list(self) -> ErrorList:
		return ErrorList(self._instance.GetAllErrorsList())
	def get_current_position(self) -> CurrentPosition:
		return CurrentPosition(self._instance.GetCurrentPosition())
	def get_io_state(self, progress: typing.Any=None) -> IOState:
		return IOState(self._instance.GetIOState(progress))
	def get_safety_status(self) -> SafetyStatus:
		return SafetyStatus(self._instance.GetSafetyStatus())
	def get_program_states(self) -> ProgramStates:
		return ProgramStates(self._instance.GetProgramStates())
	def get_variables_from_file(self, variableFileName: str) -> GenericVariableFile:
		return GenericVariableFile(self._instance.GetVariablesFromFile(variableFileName))
	def enumerate_variable_files(self) -> typing.List[FtpListItem]:
		return [FtpListItem(x) for x in self._instance.EnumerateVariableFiles()]
	def get_all_variables(self, progress: typing.Any=None) -> VariableFileList:
		return VariableFileList(self._instance.GetAllVariables(progress))
	@property
	def ip(self) -> str:
		return self._instance.IP
	@property
	def connected(self) -> bool:
		return self._instance.Connected
	@property
	def direct_file_handling(self) -> FtpDirectFileHandling:
		return FtpDirectFileHandling(self._instance.DirectFileHandling)
	@property
	def known_variable_files(self) -> FtpKnownVariableFiles:
		return FtpKnownVariableFiles(self._instance.KnownVariableFiles)
