import typing
from underautomation.fanuc.stream_motion.data.robot_status_flags import RobotStatusFlags
from UnderAutomation.Fanuc.StreamMotion.Data import RobotStatus as robot_status
from UnderAutomation.Fanuc.StreamMotion.Data import RobotStatusFlags as robot_status_flags

class RobotStatus:
	'''Robot status from state packet'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_status()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def raw_value(self) -> int:
		'''Raw status byte'''
		return self._instance.RawValue

	@property
	def flags(self) -> RobotStatusFlags:
		'''Status flags'''
		return RobotStatusFlags(int(self._instance.Flags))

	@property
	def ready_for_commands(self) -> bool:
		'''Robot is ready to receive command packets'''
		return self._instance.ReadyForCommands

	@property
	def command_received(self) -> bool:
		'''Robot has received at least one command packet'''
		return self._instance.CommandReceived

	@property
	def system_ready(self) -> bool:
		'''System ready (SYSRDY)'''
		return self._instance.SystemReady

	@property
	def in_motion(self) -> bool:
		'''Robot is in motion'''
		return self._instance.InMotion

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
