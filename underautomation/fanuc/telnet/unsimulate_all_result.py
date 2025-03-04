import typing
from underautomation.fanuc.telnet.base_result import BaseResult
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import UnsimulateAllResult as unsimulate_all_result

class UnsimulateAllResult(BaseResult):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = unsimulate_all_result()
		else:
			self._instance = _internal
