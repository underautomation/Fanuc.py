import typing
from underautomation.fanuc.rmi.internal.rmi_client_base import RmiClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi import RmiClient as rmi_client

class RmiClient(RmiClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, port: int=16001, readTimeoutMs: int=3000, writeTimeoutMs: int=3000) -> None:
		self._instance.Connect(ip, port, readTimeoutMs, writeTimeoutMs)
