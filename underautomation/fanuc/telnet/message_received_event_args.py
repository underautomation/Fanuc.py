import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import MessageReceivedEventArgs as message_received_event_args

class MessageReceivedEventArgs:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = message_received_event_args()
		else:
			self._instance = _internal
	@property
	def is_reset(self) -> bool:
		return self._instance.IsReset
	@property
	def message(self) -> str:
		return self._instance.Message
	@message.setter
	def message(self, value: str):
		self._instance.Message = value
