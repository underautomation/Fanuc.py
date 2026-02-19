import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.task_state import TaskState
from UnderAutomation.Fanuc.Ftp.Diagnosis import ProgramStates as program_states

class ProgramStates(IFanucContent):
	'''Implements IFanucContent to hold a collection of task states.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_states()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def task_states(self) -> typing.List[TaskState]:
		'''Array of task states currently on the controller.'''
		return [TaskState(x) for x in self._instance.TaskStates]

	@task_states.setter
	def task_states(self, value: typing.List[TaskState]):
		self._instance.TaskStates = value

	@property
	def name(self) -> str:
		'''File name: prgstate.dg'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramStates):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
