import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import GetVariableResult as get_variable_result

class GetVariableResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_variable_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def raw_value(self) -> str:
		return self._instance.RawValue
