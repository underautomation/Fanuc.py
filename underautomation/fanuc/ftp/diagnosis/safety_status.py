import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from UnderAutomation.Fanuc.Ftp.Diagnosis import SafetyStatus as safety_status

class SafetyStatus(IFanucContent):
	'''Safety status informations'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_status()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def external_e_stop(self) -> bool:
		'''External emergency stop active'''
		return self._instance.ExternalEStop

	@property
	def sope_stop(self) -> bool:
		'''Emergency stop active by SOP signal'''
		return self._instance.SOPEStop

	@property
	def tpe_stop(self) -> bool:
		'''Emergency stop active on teach peandant'''
		return self._instance.TPEStop

	@property
	def hand_broken(self) -> bool:
		'''Hand broken signal is active'''
		return self._instance.HandBroken

	@property
	def over_travel(self) -> bool:
		'''Over travel limit is active'''
		return self._instance.OverTravel

	@property
	def low_air_alarm(self) -> bool:
		'''Low air pressure alarm is active'''
		return self._instance.LowAirAlarm

	@property
	def fence_open(self) -> bool:
		'''Safety fence is open'''
		return self._instance.FenceOpen

	@property
	def belt_broken(self) -> bool:
		'''Belt broken signal is active'''
		return self._instance.BeltBroken

	@property
	def tp_enable(self) -> bool:
		'''Teach pendant is enabled'''
		return self._instance.TPEnable

	@property
	def tp_deadman(self) -> bool:
		'''The deadman switch of the teach pendant is active'''
		return self._instance.TPDeadman

	@property
	def svoff_detect(self) -> bool:
		'''Servo off detection is active'''
		return self._instance.SVOFFDetect

	@property
	def non_teacher_enb(self) -> bool:
		'''Non-teacher enable signal is active'''
		return self._instance.NonTeacherEnb

	@property
	def name(self) -> str:
		'''File name : sftysig.dg'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
