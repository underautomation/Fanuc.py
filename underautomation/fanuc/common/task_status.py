import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import TaskStatus as task_status

class TaskStatus(int):
	Unknown = int(task_status.Unknown)
	Running = int(task_status.Running)
	Paused = int(task_status.Paused)
	Aborted = int(task_status.Aborted)

	def __repr__(self):
		for name, value in vars(TaskStatus).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
