import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import AddBreakpointResult as add_breakpoint_result

class AddBreakpointResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = add_breakpoint_result()
		else:
			self._instance = _internal
