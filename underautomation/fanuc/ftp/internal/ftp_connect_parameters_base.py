import typing
from UnderAutomation.Fanuc.Ftp.Internal import FtpConnectParametersBase as ftp_connect_parameters_base

class FtpConnectParametersBase:
	'''Parameters to connect to Fanuc controller FTP server'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def ftp_user(self) -> str:
		'''FTP user'''
		return self._instance.FtpUser

	@ftp_user.setter
	def ftp_user(self, value: str):
		self._instance.FtpUser = value

	@property
	def ftp_password(self) -> str:
		'''FTP password associated to the user'''
		return self._instance.FtpPassword

	@ftp_password.setter
	def ftp_password(self, value: str):
		self._instance.FtpPassword = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
