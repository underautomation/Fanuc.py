import typing
from underautomation.fanuc.telnet.tp_coordinates import TpCoordinates
from UnderAutomation.Fanuc.Telnet import TpCoordinatesReceivedEventArgs as tp_coordinates_received_event_args
from UnderAutomation.Fanuc.Telnet import TpCoordinates as tp_coordinates

class TpCoordinatesReceivedEventArgs:
	'''Event arguments for TP coordinates received events.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_coordinates_received_event_args()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def coord(self) -> TpCoordinates:
		'''Gets the TP coordinate system received.'''
		return TpCoordinates(int(self._instance.Coord))

	@coord.setter
	def coord(self, value: TpCoordinates):
		self._instance.Coord = tp_coordinates(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpCoordinatesReceivedEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
