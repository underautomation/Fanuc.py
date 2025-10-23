import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
from underautomation.fanuc.ftp.diagnosis.io_state import IOState
from underautomation.fanuc.ftp.diagnosis.features import Features
from underautomation.fanuc.ftp.diagnosis.program_states import ProgramStates
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import SummaryDiagnosis as summary_diagnosis

class SummaryDiagnosis(IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = summary_diagnosis()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def current_position(self) -> CurrentPosition:
		return CurrentPosition(self._instance.CurrentPosition)
	@property
	def safety(self) -> SafetyStatus:
		return SafetyStatus(self._instance.Safety)
	@property
	def i_os(self) -> IOState:
		return IOState(self._instance.IOs)
	@property
	def features(self) -> Features:
		return Features(self._instance.Features)
	@property
	def program_states(self) -> ProgramStates:
		return ProgramStates(self._instance.ProgramStates)
