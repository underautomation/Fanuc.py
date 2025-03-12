import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import Breakpoint as breakpoint

class Breakpoint:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = breakpoint()
		else:
			self._instance = _internal
	@property
	def line(self) -> int:
		return self._instance.Line
