import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import TaskStatus as task_status

class TaskStatus(int):
	Unknown = task_status.Unknown
	Running = task_status.Running
	Paused = task_status.Paused
	Aborted = task_status.Aborted
