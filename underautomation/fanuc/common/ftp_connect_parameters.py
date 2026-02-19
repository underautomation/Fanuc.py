import typing
from underautomation.fanuc.ftp.internal.ftp_connect_parameters_base import FtpConnectParametersBase
from UnderAutomation.Fanuc.Common import FtpConnectParameters as ftp_connect_parameters

class FtpConnectParameters(FtpConnectParametersBase):
	'''Memory access parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should enable memory access for this connection (default: true)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
