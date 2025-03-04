import typing
from underautomation.fanuc.snpx.internal.packet_type import PacketType
from underautomation.fanuc.snpx.internal.message_type import MessageType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import PacketBase as packet_base

class PacketBase:
	def __init__(self, buffer: typing.List[int], _internal = 0):
		if(_internal == 0):
			self._instance = packet_base(buffer)
		else:
			self._instance = _internal
	@staticmethod
	def extra_length_from_header_buffer(buffer: typing.List[int]) -> int:
		return packet_base.ExtraLengthFromHeaderBuffer(buffer)
	def get_bytes(self) -> typing.List[int]:
		return self._instance.GetBytes()
	@property
	def header(self) -> typing.List[int]:
		return self._instance.Header
	@property
	def packet_type(self) -> PacketType:
		return PacketType(self._instance.PacketType)
	@packet_type.setter
	def packet_type(self, value: PacketType):
		self._instance.PacketType = value
	@property
	def extra_length(self) -> int:
		return self._instance.ExtraLength
	@property
	def unknown_8(self) -> int:
		return self._instance.Unknown_8
	@unknown_8.setter
	def unknown_8(self, value: int):
		self._instance.Unknown_8 = value
	@property
	def unknown_16(self) -> int:
		return self._instance.Unknown_16
	@unknown_16.setter
	def unknown_16(self, value: int):
		self._instance.Unknown_16 = value
	@property
	def second(self) -> int:
		return self._instance.Second
	@second.setter
	def second(self, value: int):
		self._instance.Second = value
	@property
	def minute(self) -> int:
		return self._instance.Minute
	@minute.setter
	def minute(self, value: int):
		self._instance.Minute = value
	@property
	def hour(self) -> int:
		return self._instance.Hour
	@hour.setter
	def hour(self, value: int):
		self._instance.Hour = value
	@property
	def message_type(self) -> MessageType:
		return MessageType(self._instance.MessageType)
	@message_type.setter
	def message_type(self, value: MessageType):
		self._instance.MessageType = value
	@property
	def mailbox_source(self) -> int:
		return self._instance.MailboxSource
	@mailbox_source.setter
	def mailbox_source(self, value: int):
		self._instance.MailboxSource = value
	@property
	def mailbox_destination(self) -> int:
		return self._instance.MailboxDestination
	@mailbox_destination.setter
	def mailbox_destination(self, value: int):
		self._instance.MailboxDestination = value
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
	def sequence_number(self) -> int:
		return self._instance.SequenceNumber
	@sequence_number.setter
	def sequence_number(self, value: int):
		self._instance.SequenceNumber = value
	@property
	def extra_payload(self) -> typing.List[int]:
		return self._instance.ExtraPayload
	@extra_payload.setter
	def extra_payload(self, value: typing.List[int]):
		self._instance.ExtraPayload = value
	@property
	def payload(self) -> typing.List[int]:
		return self._instance.Payload
	@payload.setter
	def payload(self, value: typing.List[int]):
		self._instance.Payload = value
	@property
	def actual_payload(self) -> typing.List[int]:
		return self._instance.ActualPayload
	@property
	def heade_r__length(self) -> int:
		return self._instance.HEADER_LENGTH
	@heade_r__length.setter
	def heade_r__length(self, value: int):
		self._instance.HEADER_LENGTH = value
