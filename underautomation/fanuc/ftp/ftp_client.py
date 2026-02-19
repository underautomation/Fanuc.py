import typing
from underautomation.fanuc.ftp.internal.ftp_client_base import FtpClientBase
from UnderAutomation.Fanuc.Ftp import FtpClient as ftp_client

class FtpClient(FtpClientBase):
	'''FTP Client connection to a robot'''
	def __init__(self, _internal = 0):
		'''Instanciate a new FTP client connection'''
		if(_internal == 0):
			self._instance = ftp_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, user: str, password: str) -> None:
		'''Connect to a robot

		:param ip: IP or network name of the robot
		:param user: FTP username
		:param password: FTP password for username
		'''
		self._instance.Connect(ip, user, password)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
