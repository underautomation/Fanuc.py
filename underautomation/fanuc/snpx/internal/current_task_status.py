import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.robot_task_status import RobotTaskStatus
from UnderAutomation.Fanuc.Snpx.Internal import CurrentTaskStatus as current_task_status

class CurrentTaskStatus(SnpxAssignableElements2[RobotTaskStatus, int]):
	'''Provides access to the current task (program) status on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_task_status()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentTaskStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
