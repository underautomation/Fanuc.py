import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import CurrentAlarmsRequest as current_alarms_request

class CurrentAlarmsRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_alarms_request()
		else:
			self._instance = _internal
	@property
	def is_history(self) -> bool:
		return self._instance.IsHistory
	@is_history.setter
	def is_history(self, value: bool):
		self._instance.IsHistory = value
	@property
	def index(self) -> int:
		return self._instance.Index
	@index.setter
	def index(self, value: int):
		self._instance.Index = value
