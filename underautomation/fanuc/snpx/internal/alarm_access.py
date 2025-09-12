import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.robot_alarm import RobotAlarm
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import AlarmAccess as alarm_access

class AlarmAccess(SnpxAssignableElements2[RobotAlarm, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = alarm_access()
		else:
			self._instance = _internal
