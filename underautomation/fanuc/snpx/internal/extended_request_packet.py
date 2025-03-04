import typing
from underautomation.fanuc.snpx.internal.extended_packet_base import ExtendedPacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ExtendedRequestPacket as extended_request_packet

class ExtendedRequestPacket(ExtendedPacketBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = extended_request_packet()
		else:
			self._instance = _internal
	@property
	def index(self) -> int:
		return self._instance.Index
	@index.setter
	def index(self, value: int):
		self._instance.Index = value
	@property
	def count(self) -> int:
		return self._instance.Count
	@count.setter
	def count(self, value: int):
		self._instance.Count = value
