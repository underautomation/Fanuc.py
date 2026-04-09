from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.internal.cgtp_client_base import CgtpClientBase
from UnderAutomation.Fanuc.Cgtp import CgtpClient as cgtp_client

class CgtpClient(CgtpClientBase):
	'''Standalone CGTP Web Server client for direct use without FanucRobot.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the CGTP Web Server client.'''
		if(_internal == 0):
			self._instance = cgtp_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: int=3080, requestTimeoutMs: int=3000, login: str=None, password: str=None) -> None:
		'''Connect to the CGTP Web Server on the controller.

		:param ip: Controller IP address or hostname.
		:param port: HTTP port number (default: 3080).
		:param requestTimeoutMs: Request timeout in milliseconds (default: 3000).
		:param login: Login for HTTP Basic authentication (optional).
		:param password: Password for HTTP Basic authentication (optional).
		'''
		self._instance.Connect(ip, port, requestTimeoutMs, login, password)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
