import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.robot_task_status import RobotTaskStatus
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import CurrentTaskStatus as current_task_status

class CurrentTaskStatus(SnpxAssignableElements2[RobotTaskStatus, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_task_status()
		else:
			self._instance = _internal
