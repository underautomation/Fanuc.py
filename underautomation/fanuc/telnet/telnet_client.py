import typing
from underautomation.fanuc.telnet.internal.telnet_client_base import TelnetClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import TelnetClient as telnet_client

class TelnetClient(TelnetClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, telnetKclPassword: str) -> None:
		self._instance.Connect(ip, telnetKclPassword)
