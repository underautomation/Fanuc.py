import typing
from underautomation.fanuc.common.task_status import TaskStatus
from underautomation.fanuc.common.program_type import ProgramType
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import TaskInformationResult as task_information_result
from UnderAutomation.Fanuc.Common import TaskStatus as task_status
from UnderAutomation.Fanuc.Common import ProgramType as program_type

class TaskInformationResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_information_result()
		else:
			self._instance = _internal

	@property
	def task_name(self) -> str:
		'''Gets the name of the task.'''
		return self._instance.TaskName

	@property
	def task_number(self) -> int:
		'''Gets the task number.'''
		return self._instance.TaskNumber

	@property
	def task_status_str(self) -> str:
		'''Gets the task status as a string.'''
		return self._instance.TaskStatusStr

	@property
	def task_status(self) -> TaskStatus:
		'''Gets the task status.'''
		return TaskStatus(int(self._instance.TaskStatus))

	@property
	def routine_name(self) -> str:
		'''Gets the name of the routine.'''
		return self._instance.RoutineName

	@property
	def current_line(self) -> int:
		'''Gets the current line number.'''
		return self._instance.CurrentLine

	@property
	def program_type(self) -> ProgramType:
		'''Gets the type of the program.'''
		return ProgramType(int(self._instance.ProgramType))

	@property
	def hold_conditions(self) -> str:
		'''Gets the hold conditions.'''
		return self._instance.HoldConditions

	@property
	def invisible_task(self) -> bool:
		'''Gets a value indicating whether the task is invisible.'''
		return self._instance.InvisibleTask

	@property
	def system_task(self) -> bool:
		'''Gets a value indicating whether the task is a system task.'''
		return self._instance.SystemTask

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TaskInformationResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
