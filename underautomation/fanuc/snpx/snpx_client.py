import typing
from underautomation.fanuc.snpx.internal.snpx_client_base import SnpxClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx import SnpxClient as snpx_client

class SnpxClient(SnpxClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, port: int=60008) -> None:
		self._instance.Connect(ip, port)
