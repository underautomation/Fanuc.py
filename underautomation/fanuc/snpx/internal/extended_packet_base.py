import typing
from underautomation.fanuc.snpx.internal.service_request_code import ServiceRequestCode
from underautomation.fanuc.snpx.internal.segment_selector import SegmentSelector
from underautomation.fanuc.snpx.internal.packet_base import PacketBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import ExtendedPacketBase as extended_packet_base

class ExtendedPacketBase(PacketBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = extended_packet_base()
		else:
			self._instance = _internal
	@property
	def packet_number(self) -> int:
		return self._instance.PacketNumber
	@packet_number.setter
	def packet_number(self, value: int):
		self._instance.PacketNumber = value
	@property
	def total_packet_number(self) -> int:
		return self._instance.TotalPacketNumber
	@total_packet_number.setter
	def total_packet_number(self, value: int):
		self._instance.TotalPacketNumber = value
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
	def payload(self) -> typing.List[int]:
		return self._instance.Payload
	@payload.setter
	def payload(self, value: typing.List[int]):
		self._instance.Payload = value
	@property
	def actual_payload(self) -> typing.List[int]:
		return self._instance.ActualPayload
