import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import RobotStatusFlags as robot_status_flags

class RobotStatusFlags(int):
	ReadyForCommands = robot_status_flags.ReadyForCommands
	CommandReceived = robot_status_flags.CommandReceived
	SystemReady = robot_status_flags.SystemReady
	InMotion = robot_status_flags.InMotion
