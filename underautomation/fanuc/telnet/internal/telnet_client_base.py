from __future__ import annotations
import typing
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.telnet.tp_coordinates import TpCoordinates
from underautomation.fanuc.common.kcl.kcl_client_base import KclClientBase
from underautomation.fanuc.telnet.raw_data_received_event_args import RawDataReceivedEventArgs
from underautomation.fanuc.telnet.tp_coordinates_received_event_args import TpCoordinatesReceivedEventArgs
from underautomation.fanuc.telnet.message_received_event_args import MessageReceivedEventArgs
from underautomation.fanuc.telnet.kcl_client_error_event_args import KclClientErrorEventArgs
from underautomation.fanuc.telnet.command_sent_event_args import CommandSentEventArgs
from underautomation.fanuc.telnet.kcl_command_received import KclCommandReceived
from UnderAutomation.Fanuc.Telnet.Internal import TelnetClientBase as telnet_client_base
from UnderAutomation.Fanuc.Common import Languages as languages
from UnderAutomation.Fanuc.Telnet import TpCoordinates as tp_coordinates

class TelnetClientBase(KclClientBase):
	'''Base class for Telnet KCL client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_client_base()
		else:
			self._instance = _internal

	def raw_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RawDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def string_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.StringDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def tp_coordinates_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.TpCoordinatesReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.MessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def error_occured(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ErrorOccured+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def command_sent(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CommandSent+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def command_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CommandReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def poll_and_get_updated_connected_state(self) -> bool:
		'''Checks the actual connection status via an active socket polling

		:returns: True if the connection is still open after checking via polling
		'''
		return self._instance.PollAndGetUpdatedConnectedState()

	def disconnect(self) -> None:
		'''Disconnect Telnet client from robot'''
		self._instance.Disconnect()

	@property
	def ip(self) -> str:
		'''Connect robot IP address or host name'''
		return self._instance.IP

	@property
	def language(self) -> Languages:
		'''Controller language (default is English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def tp_coordinates(self) -> TpCoordinates:
		'''Gets the current Teach Pendant coordinate system.'''
		return TpCoordinates(int(self._instance.TpCoordinates))

	@property
	def connected(self) -> bool:
		'''Is Telnet client connected'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TelnetClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
