import typing
from underautomation.fanuc.snpx.internal.short_packet_base import ShortPacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ShortRequestPacket as short_request_packet

class ShortRequestPacket(ShortPacketBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = short_request_packet()
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
	@property
	def payload(self) -> typing.List[int]:
		return self._instance.Payload
	@payload.setter
	def payload(self, value: typing.List[int]):
		self._instance.Payload = value
	@property
	def actual_payload(self) -> typing.List[int]:
		return self._instance.ActualPayload
