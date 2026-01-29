import typing
from underautomation.fanuc.stream_motion.data.robot_status_flags import RobotStatusFlags
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import RobotStatus as robot_status

class RobotStatus:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_status()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def raw_value(self) -> int:
		return self._instance.RawValue
	@property
	def flags(self) -> RobotStatusFlags:
		return RobotStatusFlags(self._instance.Flags)
	@property
	def ready_for_commands(self) -> bool:
		return self._instance.ReadyForCommands
	@property
	def command_received(self) -> bool:
		return self._instance.CommandReceived
	@property
	def system_ready(self) -> bool:
		return self._instance.SystemReady
	@property
	def in_motion(self) -> bool:
		return self._instance.InMotion
