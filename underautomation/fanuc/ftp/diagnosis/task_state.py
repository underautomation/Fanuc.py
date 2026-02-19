import typing
from underautomation.fanuc.common.task_status import TaskStatus
from underautomation.fanuc.ftp.diagnosis.task_history_data import TaskHistoryData
from UnderAutomation.Fanuc.Ftp.Diagnosis import TaskState as task_state
from UnderAutomation.Fanuc.Common import TaskStatus as task_status

class TaskState:
	'''Represents a single task's state.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_state()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def number(self) -> int:
		'''Task number.'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def name(self) -> str:
		'''Task name.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def status(self) -> TaskStatus:
		'''Current execution status of the task.'''
		return TaskStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: TaskStatus):
		self._instance.Status = task_status(int(value))

	@property
	def history(self) -> typing.List[TaskHistoryData]:
		'''Call stack history frames for the task.'''
		return [TaskHistoryData(x) for x in self._instance.History]

	@history.setter
	def history(self, value: typing.List[TaskHistoryData]):
		self._instance.History = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TaskState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
