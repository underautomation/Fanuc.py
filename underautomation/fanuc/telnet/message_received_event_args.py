import typing
from UnderAutomation.Fanuc.Telnet import MessageReceivedEventArgs as message_received_event_args

class MessageReceivedEventArgs:
	'''Event arguments for message received events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = message_received_event_args()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def is_reset(self) -> bool:
		'''Gets a value indicating whether the message is a reset (empty message).'''
		return self._instance.IsReset

	@property
	def message(self) -> str:
		'''Gets the message received from the controller.'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MessageReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
