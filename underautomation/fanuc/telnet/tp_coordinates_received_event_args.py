import typing
from underautomation.fanuc.telnet.tp_coordinates import TpCoordinates
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import TpCoordinatesReceivedEventArgs as tp_coordinates_received_event_args

class TpCoordinatesReceivedEventArgs:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_coordinates_received_event_args()
		else:
			self._instance = _internal
	@property
	def coord(self) -> TpCoordinates:
		return TpCoordinates(self._instance.Coord)
	@coord.setter
	def coord(self, value: TpCoordinates):
		self._instance.Coord = value
