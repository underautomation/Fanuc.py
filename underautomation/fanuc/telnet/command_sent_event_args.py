import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import CommandSentEventArgs as command_sent_event_args

class CommandSentEventArgs:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = command_sent_event_args()
		else:
			self._instance = _internal
	@property
	def command(self) -> str:
		return self._instance.Command
	@command.setter
	def command(self, value: str):
		self._instance.Command = value
