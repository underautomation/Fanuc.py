import typing
from underautomation.fanuc.common.task_status import TaskStatus
from underautomation.fanuc.ftp.diagnosis.task_history_data import TaskHistoryData
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import TaskState as task_state

class TaskState:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_state()
		else:
			self._instance = _internal
	@property
	def number(self) -> int:
		return self._instance.Number
	@number.setter
	def number(self, value: int):
		self._instance.Number = value
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def status(self) -> TaskStatus:
		return TaskStatus(self._instance.Status)
	@status.setter
	def status(self, value: TaskStatus):
		self._instance.Status = value
	@property
	def history(self) -> typing.List[TaskHistoryData]:
		return [TaskHistoryData(x) for x in self._instance.History]
	@history.setter
	def history(self, value: typing.List[TaskHistoryData]):
		self._instance.History = value
