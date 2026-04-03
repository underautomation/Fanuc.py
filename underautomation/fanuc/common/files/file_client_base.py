from __future__ import annotations
import typing
from underautomation.fanuc.common.files.known_variable_files import KnownVariableFiles
from underautomation.fanuc.common.files.diagnosis.summary_diagnosis import SummaryDiagnosis
from underautomation.fanuc.common.files.list.error_list import ErrorList
from underautomation.fanuc.common.files.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.common.files.diagnosis.io_state import IOState
from underautomation.fanuc.common.files.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.common.files.diagnosis.program_states import ProgramStates
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from underautomation.fanuc.common.files.variables.variable_file_list import VariableFileList
from underautomation.fanuc.common.files.on_progress_delegate import OnProgressDelegate
from UnderAutomation.Fanuc.Common.Files import FileClientBase as file_client_base

class FileClientBase:
	'''Base class for Fanuc file client. It provides methods to read and parse known files such as summary diagnostic, error list, current position, ...'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_client_base()
		else:
			self._instance = _internal

	def get_summary_diagnostic(self) -> SummaryDiagnosis:
		'''Get controller status (position, safety, ios, ...)'''
		return SummaryDiagnosis(self._instance.GetSummaryDiagnostic())

	def get_all_errors_list(self) -> ErrorList:
		'''Get a list of all errors logged by the controller'''
		return ErrorList(self._instance.GetAllErrorsList())

	def get_current_position(self) -> CurrentPosition:
		'''Get current robot position of each robot handled by this controller'''
		return CurrentPosition(self._instance.GetCurrentPosition())

	def get_io_state(self) -> IOState:
		'''Get controller IO State'''
		return IOState(self._instance.GetIOState())

	def get_safety_status(self) -> SafetyStatus:
		'''Get controller safety status'''
		return SafetyStatus(self._instance.GetSafetyStatus())

	def get_program_states(self) -> ProgramStates:
		'''Get controller program states'''
		return ProgramStates(self._instance.GetProgramStates())

	def get_variables_from_file(self, variableFileName: str) -> GenericVariableFile:
		'''Get and parse a variable file from its name'''
		return GenericVariableFile(self._instance.GetVariablesFromFile(variableFileName))

	def enumerate_variable_file_names(self) -> typing.List[str]:
		'''Get the list of all variable file names available on the controller'''
		return self._instance.EnumerateVariableFileNames()

	def get_all_variables(self, progress: OnProgressDelegate=None) -> VariableFileList:
		'''Get the list of all variables on the controller. All variables files are read and decoded'''
		return VariableFileList(self._instance.GetAllVariables(progress._instance if progress else None))

	@property
	def known_variable_files(self) -> KnownVariableFiles:
		'''A list of method to read specific files'''
		return KnownVariableFiles(self._instance.KnownVariableFiles)

	@property
	def ip(self) -> str:
		'''IP address of the controller'''
		return self._instance.IP

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
