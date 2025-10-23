import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.diagnosis.task_state import TaskState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import ProgramStates as program_states

class ProgramStates(IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_states()
		else:
			self._instance = _internal
	@property
	def task_states(self) -> typing.List[TaskState]:
		return [TaskState(x) for x in self._instance.TaskStates]
	@task_states.setter
	def task_states(self, value: typing.List[TaskState]):
		self._instance.TaskStates = value
	@property
	def name(self) -> str:
		return self._instance.Name
