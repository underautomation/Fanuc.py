from __future__ import annotations
import typing
from underautomation.fanuc.common.kcl.custom_command_result import CustomCommandResult
from underautomation.fanuc.common.kcl.kcl_client_base import KclClientBase
from UnderAutomation.Fanuc.Cgtp.Internal import CgtpKclClient as cgtp_kcl_client

class CgtpKclClient(KclClientBase):
	'''KCL client implementation using the CGTP Web Server. Provides KCL commands over HTTP endpoints.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_kcl_client()
		else:
			self._instance = _internal

	def send_custom_command_unsafe(self, command: str) -> CustomCommandResult:
		'''Sends a custom KCL command in Unsafe mode. Success or failure cannot be determined from the result.

		:param command: Custom command to send
		'''
		return CustomCommandResult(self._instance.SendCustomCommandUnsafe(command))

	@property
	def enabled(self) -> bool:
		'''Indicates whether the KCL client is currently connected.'''
		return self._instance.Enabled

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpKclClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
