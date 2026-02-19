import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.ftp.diagnosis.io_state import IOState
from underautomation.fanuc.ftp.diagnosis.features import Features
from underautomation.fanuc.ftp.diagnosis.program_states import ProgramStates
from UnderAutomation.Fanuc.Ftp.Diagnosis import SummaryDiagnosis as summary_diagnosis

class SummaryDiagnosis(IFanucContent):
	'''All diagnosis information'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = summary_diagnosis()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''File name : summary.dg'''
		return self._instance.Name

	@property
	def current_position(self) -> CurrentPosition:
		'''Current position of each robots and groups handled by this controller'''
		return CurrentPosition(self._instance.CurrentPosition)

	@property
	def safety(self) -> SafetyStatus:
		'''Controller safety information'''
		return SafetyStatus(self._instance.Safety)

	@property
	def i_os(self) -> IOState:
		'''Controller IO status'''
		return IOState(self._instance.IOs)

	@property
	def features(self) -> Features:
		'''Controller features status'''
		return Features(self._instance.Features)

	@property
	def program_states(self) -> ProgramStates:
		'''Controller program states'''
		return ProgramStates(self._instance.ProgramStates)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SummaryDiagnosis):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
