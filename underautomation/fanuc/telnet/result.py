import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import Result as result

class Result:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def error_text(self) -> str:
		return self._instance.ErrorText
	@property
	def succeed(self) -> bool:
		return self._instance.Succeed
	@property
	def kcl_command(self) -> str:
		return self._instance.KclCommand
