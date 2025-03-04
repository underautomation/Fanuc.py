import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FtpConnectParametersBase as ftp_connect_parameters_base

class FtpConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def ftp_user(self) -> str:
		return self._instance.FtpUser
	@ftp_user.setter
	def ftp_user(self, value: str):
		self._instance.FtpUser = value
	@property
	def ftp_password(self) -> str:
		return self._instance.FtpPassword
	@ftp_password.setter
	def ftp_password(self, value: str):
		self._instance.FtpPassword = value
