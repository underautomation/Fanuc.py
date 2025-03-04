import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import VariableResult as variable_result

class VariableResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_result()
		else:
			self._instance = _internal
