import typing
from underautomation.fanuc.ftp.internal.ftp_client_base import FtpClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp import FtpClient as ftp_client

class FtpClient(FtpClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, user: str, password: str) -> None:
		self._instance.Connect(ip, user, password)
