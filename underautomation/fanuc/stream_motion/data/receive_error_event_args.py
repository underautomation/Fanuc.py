import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import ReceiveErrorEventArgs as receive_error_event_args

class ReceiveErrorEventArgs:
	def __init__(self, exception: typing.Any, isStreaming: bool, _internal = 0):
		if(_internal == 0):
			self._instance = receive_error_event_args(exception, isStreaming)
		else:
			self._instance = _internal
	@property
	def exception(self) -> typing.Any:
		return self._instance.Exception
	@property
	def is_streaming(self) -> bool:
		return self._instance.IsStreaming
