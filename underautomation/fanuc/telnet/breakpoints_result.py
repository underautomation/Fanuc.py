import typing
from underautomation.fanuc.telnet.breakpoint import Breakpoint
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import BreakpointsResult as breakpoints_result

class BreakpointsResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = breakpoints_result()
		else:
			self._instance = _internal
	@property
	def breakpoints(self) -> typing.List[Breakpoint]:
		return [Breakpoint(x) for x in self._instance.Breakpoints]
