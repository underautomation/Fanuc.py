import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import RobotTaskState as robot_task_state

class RobotTaskState(int):
	Stopped = robot_task_state.Stopped
	Paused = robot_task_state.Paused
	Running = robot_task_state.Running
