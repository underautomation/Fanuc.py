import typing
from UnderAutomation.Fanuc.Telnet import CommandSentEventArgs as command_sent_event_args

class CommandSentEventArgs:
	'''Event arguments for command sent events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = command_sent_event_args()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def command(self) -> str:
		'''Gets the command that was sent.'''
		return self._instance.Command

	@command.setter
	def command(self, value: str):
		self._instance.Command = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommandSentEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
