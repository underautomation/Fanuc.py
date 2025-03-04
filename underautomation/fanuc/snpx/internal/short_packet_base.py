import typing
from underautomation.fanuc.snpx.internal.service_request_code import ServiceRequestCode
from underautomation.fanuc.snpx.internal.segment_selector import SegmentSelector
from underautomation.fanuc.snpx.internal.packet_base import PacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ShortPacketBase as short_packet_base

class ShortPacketBase(PacketBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = short_packet_base()
		else:
			self._instance = _internal
	@property
	def service_request_code(self) -> ServiceRequestCode:
		return ServiceRequestCode(self._instance.ServiceRequestCode)
	@service_request_code.setter
	def service_request_code(self, value: ServiceRequestCode):
		self._instance.ServiceRequestCode = value
	@property
	def segment_selector(self) -> SegmentSelector:
		return SegmentSelector(self._instance.SegmentSelector)
	@segment_selector.setter
	def segment_selector(self, value: SegmentSelector):
		self._instance.SegmentSelector = value
	@property
	def actual_payload(self) -> typing.List[int]:
		return self._instance.ActualPayload
