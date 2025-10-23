import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import SafetyStatus as safety_status

class SafetyStatus(IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_status()
		else:
			self._instance = _internal
	@property
	def external_e_stop(self) -> bool:
		return self._instance.ExternalEStop
	@property
	def sope_stop(self) -> bool:
		return self._instance.SOPEStop
	@property
	def tpe_stop(self) -> bool:
		return self._instance.TPEStop
	@property
	def hand_broken(self) -> bool:
		return self._instance.HandBroken
	@property
	def over_travel(self) -> bool:
		return self._instance.OverTravel
	@property
	def low_air_alarm(self) -> bool:
		return self._instance.LowAirAlarm
	@property
	def fence_open(self) -> bool:
		return self._instance.FenceOpen
	@property
	def belt_broken(self) -> bool:
		return self._instance.BeltBroken
	@property
	def tp_enable(self) -> bool:
		return self._instance.TPEnable
	@property
	def tp_deadman(self) -> bool:
		return self._instance.TPDeadman
	@property
	def svoff_detect(self) -> bool:
		return self._instance.SVOFFDetect
	@property
	def non_teacher_enb(self) -> bool:
		return self._instance.NonTeacherEnb
	@property
	def name(self) -> str:
		return self._instance.Name
