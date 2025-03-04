import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import SetValueResult as set_value_result

class SetValueResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_value_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def former_value(self) -> str:
		return self._instance.FormerValue
	@property
	def new_value(self) -> str:
		return self._instance.NewValue
