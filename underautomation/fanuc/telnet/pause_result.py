import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import PauseResult as pause_result

class PauseResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pause_result()
		else:
			self._instance = _internal
