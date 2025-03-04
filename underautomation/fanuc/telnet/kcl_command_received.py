import typing
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import KclCommandReceived as kcl_command_received

class KclCommandReceived:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kcl_command_received()
		else:
			self._instance = _internal
	@property
	def result(self) -> Result:
		return Result(self._instance.Result)
	@result.setter
	def result(self, value: Result):
		self._instance.Result = value
