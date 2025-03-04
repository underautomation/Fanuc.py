import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import KclClientErrorEventArgs as kcl_client_error_event_args

class KclClientErrorEventArgs:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kcl_client_error_event_args()
		else:
			self._instance = _internal
	@property
	def exception(self) -> typing.Any:
		return self._instance.Exception
	@exception.setter
	def exception(self, value: typing.Any):
		self._instance.Exception = value
