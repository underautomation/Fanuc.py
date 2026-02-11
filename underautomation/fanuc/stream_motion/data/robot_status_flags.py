import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import RobotStatusFlags as robot_status_flags

class RobotStatusFlags(int):
	ReadyForCommands = int(robot_status_flags.ReadyForCommands)
	CommandReceived = int(robot_status_flags.CommandReceived)
	SystemReady = int(robot_status_flags.SystemReady)
	InMotion = int(robot_status_flags.InMotion)

	def __repr__(self):
		for name, value in vars(RobotStatusFlags).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
