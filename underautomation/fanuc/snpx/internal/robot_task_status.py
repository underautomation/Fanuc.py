import typing
from underautomation.fanuc.snpx.internal.robot_task_state import RobotTaskState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import RobotTaskStatus as robot_task_status

class RobotTaskStatus:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_task_status()
		else:
			self._instance = _internal
	def equals(self, other: 'RobotTaskStatus') -> bool:
		return self._instance.Equals(other._instance if other else None)
	@staticmethod
	def from_bytes(bytes: typing.List[int], start: int=0) -> 'RobotTaskStatus':
		return RobotTaskStatus(robot_task_status.FromBytes(bytes, start))
	@property
	def program_name(self) -> str:
		return self._instance.ProgramName
	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value
	@property
	def line_number(self) -> int:
		return self._instance.LineNumber
	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value
	@property
	def state(self) -> RobotTaskState:
		return RobotTaskState(self._instance.State)
	@state.setter
	def state(self, value: RobotTaskState):
		self._instance.State = value
	@property
	def caller(self) -> str:
		return self._instance.Caller
	@caller.setter
	def caller(self, value: str):
		self._instance.Caller = value
