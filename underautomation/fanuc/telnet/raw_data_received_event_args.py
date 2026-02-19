import typing
from UnderAutomation.Fanuc.Telnet import RawDataReceivedEventArgs as raw_data_received_event_args

class RawDataReceivedEventArgs:
	'''Event arguments for raw data received events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = raw_data_received_event_args()
		else:
			self._instance = _internal

	@property
	def data(self) -> str:
		'''Gets the raw data received.'''
		return self._instance.Data

	@data.setter
	def data(self, value: str):
		self._instance.Data = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RawDataReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
