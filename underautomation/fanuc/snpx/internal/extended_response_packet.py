import typing
from underautomation.fanuc.snpx.internal.extended_packet_base import ExtendedPacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ExtendedResponsePacket as extended_response_packet

class ExtendedResponsePacket(ExtendedPacketBase):
	def __init__(self, buffer: typing.List[int], _internal = 0):
		if(_internal == 0):
			self._instance = extended_response_packet(buffer)
		else:
			self._instance = _internal
