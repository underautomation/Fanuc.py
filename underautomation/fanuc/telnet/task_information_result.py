import typing
from underautomation.fanuc.common.task_status import TaskStatus
from underautomation.fanuc.common.program_type import ProgramType
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import TaskInformationResult as task_information_result

class TaskInformationResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_information_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def task_name(self) -> str:
		return self._instance.TaskName
	@property
	def task_number(self) -> int:
		return self._instance.TaskNumber
	@property
	def task_status_str(self) -> str:
		return self._instance.TaskStatusStr
	@property
	def task_status(self) -> TaskStatus:
		return TaskStatus(self._instance.TaskStatus)
	@property
	def routine_name(self) -> str:
		return self._instance.RoutineName
	@property
	def current_line(self) -> int:
		return self._instance.CurrentLine
	@property
	def program_type(self) -> ProgramType:
		return ProgramType(self._instance.ProgramType)
	@property
	def hold_conditions(self) -> str:
		return self._instance.HoldConditions
	@property
	def invisible_task(self) -> bool:
		return self._instance.InvisibleTask
	@property
	def system_task(self) -> bool:
		return self._instance.SystemTask
