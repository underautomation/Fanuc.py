import typing
from underautomation.fanuc.ftp.internal.ftp_client_base import FtpClientBase
from UnderAutomation.Fanuc.Ftp.Internal import FtpClientInternal as ftp_client_internal

class FtpClientInternal(FtpClientBase):
	'''Internal implementation of FTP Client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
