import typing
from underautomation.fanuc.snpx.internal.short_packet_base import ShortPacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ShortResponsePacket as short_response_packet

class ShortResponsePacket(ShortPacketBase):
	def __init__(self, buffer: typing.List[int], _internal = 0):
		if(_internal == 0):
			self._instance = short_response_packet(buffer)
		else:
			self._instance = _internal
	@property
	def payload(self) -> typing.List[int]:
		return self._instance.Payload
	@payload.setter
	def payload(self, value: typing.List[int]):
		self._instance.Payload = value
