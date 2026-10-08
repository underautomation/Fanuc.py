from __future__ import annotations
import typing
from underautomation.fanuc.common.files.i_fanuc_content import IFanucContent
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.common.files.i_file_reader_1 import IFileReader1
from underautomation.fanuc.common.files.variables.variable_reader import VariableReader
from underautomation.fanuc.common.files.list.error_list_reader import ErrorListReader
from underautomation.fanuc.common.files.diagnosis.summary_diagnosis_reader import SummaryDiagnosisReader
from underautomation.fanuc.common.files.diagnosis.diagnosis_reader_2 import DiagnosisReader2
from underautomation.fanuc.common.files.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.common.files.diagnosis.current_position_reader import CurrentPositionReader
from underautomation.fanuc.common.files.diagnosis.io_state import IOState
from underautomation.fanuc.common.files.diagnosis.io_state_parser import IOStateParser
from underautomation.fanuc.common.files.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.common.files.diagnosis.safety_status_parser import SafetyStatusParser
from underautomation.fanuc.common.files.diagnosis.program_states import ProgramStates
from underautomation.fanuc.common.files.diagnosis.program_states_parser import ProgramStatesParser
from UnderAutomation.Fanuc.Common.Files import FanucFileReaders as fanuc_file_readers
from UnderAutomation.Fanuc.Common import Languages as languages

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class FanucFileReaders:
	'''Contains static functions to decode Fanuc files (variables, diagnosis, listing, ...)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fanuc_file_readers()
		else:
			self._instance = _internal

	@staticmethod
	def read_file(fileName: str, language: Languages) -> IFanucContent:
		'''Read any file by path on disc, recognize it by name and decode it'''
		__r = fanuc_file_readers.ReadFile(fileName, languages(int(language)))
		return None if __r is None else IFanucContent(__r)

	@staticmethod
	def _get_readers() -> typing.List[IFileReader1]:
		'''Get the collection of all parsers'''
		__r = fanuc_file_readers.Readers
		return None if __r is None else [None if x is None else IFileReader1(x) for x in __r]

	readers = _StaticProperty(_get_readers)
	del _get_readers

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
FanucFileReaders.VariableReader = None if fanuc_file_readers.VariableReader is None else VariableReader(fanuc_file_readers.VariableReader)

# Helper to read error files like errall.ls
FanucFileReaders.ErrorListReader = None if fanuc_file_readers.ErrorListReader is None else ErrorListReader(fanuc_file_readers.ErrorListReader)

# Helper to read summary diagnosis file summary.dg
FanucFileReaders.SummaryDiagnosticReader = None if fanuc_file_readers.SummaryDiagnosticReader is None else SummaryDiagnosisReader(fanuc_file_readers.SummaryDiagnosticReader)

# Decode current position file curpos.dg
FanucFileReaders.CurrentPositionReader = None if fanuc_file_readers.CurrentPositionReader is None else DiagnosisReader2[CurrentPosition, CurrentPositionReader](fanuc_file_readers.CurrentPositionReader)

# Decode IO Status file iostate.dg
FanucFileReaders.IOStateReader = None if fanuc_file_readers.IOStateReader is None else DiagnosisReader2[IOState, IOStateParser](fanuc_file_readers.IOStateReader)

# Decode IO Status file iostate.dg
FanucFileReaders.SafetyStatusReader = None if fanuc_file_readers.SafetyStatusReader is None else DiagnosisReader2[SafetyStatus, SafetyStatusParser](fanuc_file_readers.SafetyStatusReader)

# Decode task and program states prgstate.dg
FanucFileReaders.ProgramStates = None if fanuc_file_readers.ProgramStates is None else DiagnosisReader2[ProgramStates, ProgramStatesParser](fanuc_file_readers.ProgramStates)
