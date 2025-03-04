import typing
from underautomation.fanuc.snpx.internal.robot_alarm import RobotAlarm
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.current_alarms_request import CurrentAlarmsRequest
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import CurrentAlarms as current_alarms

class CurrentAlarms(SnpxAssignableElements2[RobotAlarm, CurrentAlarmsRequest]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_alarms()
		else:
			self._instance = _internal
	def read_history(self, index: int) -> RobotAlarm:
		return RobotAlarm(self._instance.ReadHistory(index))
	def read_last_alarm(self, index: int) -> RobotAlarm:
		return RobotAlarm(self._instance.ReadLastAlarm(index))
