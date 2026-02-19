import typing
from underautomation.fanuc.telnet.internal.telnet_client_base import TelnetClientBase
from UnderAutomation.Fanuc.Telnet import TelnetClient as telnet_client

class TelnetClient(TelnetClientBase):
	'''Main class that represents a connection to a Fanuc Motoman industrial robot'''
	def __init__(self, _internal = 0):
		'''Create a new instance of a robot communication'''
		if(_internal == 0):
			self._instance = telnet_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, telnetKclPassword: str) -> None:
		'''Connect to a robot

		:param ip: IP or network name of the robot
		:param telnetKclPassword: Telnet password associated with KCL user
		'''
		self._instance.Connect(ip, telnetKclPassword)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TelnetClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
