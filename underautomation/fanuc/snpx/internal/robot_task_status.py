import typing
from underautomation.fanuc.snpx.internal.robot_task_state import RobotTaskState
from underautomation.fanuc.common.languages import Languages
from UnderAutomation.Fanuc.Snpx.Internal import RobotTaskStatus as robot_task_status
from UnderAutomation.Fanuc.Snpx.Internal import RobotTaskState as robot_task_state
from UnderAutomation.Fanuc.Common import Languages as languages

class RobotTaskStatus:
	'''Represents the status of a running task on the robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_task_status()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@staticmethod
	def from_bytes(bytes: typing.List[int], language: Languages, start: int=0) -> 'RobotTaskStatus':
		'''Creates a RobotTaskStatus from a byte array.

		:param bytes: The byte array containing task status data.
		:param language: The controller language for string decoding.
		:param start: The starting offset in the byte array.
		:returns: A RobotTaskStatus parsed from the byte data, or null if bytes is null.
		'''
		return RobotTaskStatus(robot_task_status.FromBytes(bytes, languages(int(language)), start))

	@property
	def program_name(self) -> str:
		'''Gets or sets the name of the program being executed.'''
		return self._instance.ProgramName

	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value

	@property
	def line_number(self) -> int:
		'''Gets or sets the current line number in the program.'''
		return self._instance.LineNumber

	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value

	@property
	def state(self) -> RobotTaskState:
		'''Gets or sets the current execution state of the task.'''
		return RobotTaskState(int(self._instance.State))

	@state.setter
	def state(self, value: RobotTaskState):
		self._instance.State = robot_task_state(int(value))

	@property
	def caller(self) -> str:
		'''Gets or sets the name of the calling program.'''
		return self._instance.Caller

	@caller.setter
	def caller(self, value: str):
		self._instance.Caller = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotTaskStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
