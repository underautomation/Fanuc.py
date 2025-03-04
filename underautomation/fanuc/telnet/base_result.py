import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import BaseResult as base_result

class BaseResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = base_result()
		else:
			self._instance = _internal
