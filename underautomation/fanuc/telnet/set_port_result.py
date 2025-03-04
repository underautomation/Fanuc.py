import typing
from underautomation.fanuc.telnet.set_value_result import SetValueResult
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import SetPortResult as set_port_result

class SetPortResult(SetValueResult):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_port_result()
		else:
			self._instance = _internal
