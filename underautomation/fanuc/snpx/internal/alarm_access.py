import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.robot_alarm import RobotAlarm
from UnderAutomation.Fanuc.Snpx.Internal import AlarmAccess as alarm_access

class AlarmAccess(SnpxAssignableElements2[RobotAlarm, int]):
	'''Provides access to robot alarms (active or historical) via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = alarm_access()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AlarmAccess):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
