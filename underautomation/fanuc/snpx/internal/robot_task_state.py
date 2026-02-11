import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import RobotTaskState as robot_task_state

class RobotTaskState(int):
	Stopped = int(robot_task_state.Stopped)
	Paused = int(robot_task_state.Paused)
	Running = int(robot_task_state.Running)

	def __repr__(self):
		for name, value in vars(RobotTaskState).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
