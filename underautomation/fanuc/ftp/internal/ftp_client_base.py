import typing
from underautomation.fanuc.common.languages import Languages
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
from UnderAutomation.Fanuc.Ftp.Internal import FtpClientBase as ftp_client_base
from UnderAutomation.Fanuc.Common import Languages as languages

class FtpClientBase:
	'''Base class for FTP features'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnects from FTP server'''
		self._instance.Disconnect()

	def get_summary_diagnostic(self) -> SummaryDiagnosis:
		'''Get controller status (position, safety, ios, ...)'''
		return SummaryDiagnosis(self._instance.GetSummaryDiagnostic())

	def get_all_errors_list(self) -> ErrorList:
		'''Get a list of all errors logged by the controller'''
		return ErrorList(self._instance.GetAllErrorsList())

	def get_current_position(self) -> CurrentPosition:
		'''Get current robot position of each robot handled by this controller'''
		return CurrentPosition(self._instance.GetCurrentPosition())

	def get_io_state(self, progress: typing.Any=None) -> IOState:
		return IOState(self._instance.GetIOState(progress))

	def get_safety_status(self) -> SafetyStatus:
		'''Get controller safety status'''
		return SafetyStatus(self._instance.GetSafetyStatus())

	def get_program_states(self) -> ProgramStates:
		'''Get controller program states'''
		return ProgramStates(self._instance.GetProgramStates())

	def get_variables_from_file(self, variableFileName: str) -> GenericVariableFile:
		'''Get and parse a variable file from its name'''
		return GenericVariableFile(self._instance.GetVariablesFromFile(variableFileName))

	def enumerate_variable_files(self) -> typing.List[FtpListItem]:
		'''Get a list of all variable files on controller'''
		return [FtpListItem(x) for x in self._instance.EnumerateVariableFiles()]

	def get_all_variables(self, progress: typing.Any=None) -> VariableFileList:
		return VariableFileList(self._instance.GetAllVariables(progress))

	@property
	def ip(self) -> str:
		'''Connect robot IP address or host name'''
		return self._instance.IP

	@property
	def language(self) -> Languages:
		'''Controller language (default is English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def connected(self) -> bool:
		'''Indicates that FTP connection is active'''
		return self._instance.Connected

	@property
	def direct_file_handling(self) -> FtpDirectFileHandling:
		'''Contains methods to manipulate files and folders on the controller (upload, download, delete, ...)'''
		return FtpDirectFileHandling(self._instance.DirectFileHandling)

	@property
	def known_variable_files(self) -> FtpKnownVariableFiles:
		'''A list of method to read specific files'''
		return FtpKnownVariableFiles(self._instance.KnownVariableFiles)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
