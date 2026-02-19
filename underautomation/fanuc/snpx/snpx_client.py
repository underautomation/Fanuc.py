import typing
from underautomation.fanuc.snpx.internal.snpx_client_base import SnpxClientBase
from UnderAutomation.Fanuc.Snpx import SnpxClient as snpx_client

class SnpxClient(SnpxClientBase):
	'''SNPX protocol client for communicating with Fanuc robots.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SnpxClient class.'''
		if(_internal == 0):
			self._instance = snpx_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: int=60008) -> None:
		'''Connects to a Fanuc robot using the SNPX protocol.

		:param ip: The IP address of the robot.
		:param port: The port number to connect to.
		'''
		self._instance.Connect(ip, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
