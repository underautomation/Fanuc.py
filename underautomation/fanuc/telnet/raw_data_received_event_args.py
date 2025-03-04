import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import RawDataReceivedEventArgs as raw_data_received_event_args

class RawDataReceivedEventArgs:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = raw_data_received_event_args()
		else:
			self._instance = _internal
	@property
	def data(self) -> str:
		return self._instance.Data
	@data.setter
	def data(self, value: str):
		self._instance.Data = value
