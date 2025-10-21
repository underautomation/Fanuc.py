import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import CustomCommandResult as custom_command_result

class CustomCommandResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = custom_command_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def data(self) -> str:
		return self._instance.Data
