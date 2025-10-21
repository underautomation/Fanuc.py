import typing
from underautomation.fanuc.common.telnet_connect_parameters import TelnetConnectParameters
from underautomation.fanuc.common.ftp_connect_parameters import FtpConnectParameters
from underautomation.fanuc.common.snpx_connect_parameters import SnpxConnectParameters
from underautomation.fanuc.common.rmi_connect_parameters import RmiConnectParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__),  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc import ConnectionParameters as connection_parameters

class ConnectionParameters:
	def __init__(self, address: str, _internal = 0):
		if(_internal == 0):
			self._instance = connection_parameters(address)
		else:
			self._instance = _internal
	@property
	def address(self) -> str:
		return self._instance.Address
	@address.setter
	def address(self, value: str):
		self._instance.Address = value
	@property
	def ping_before_connect(self) -> bool:
		return self._instance.PingBeforeConnect
	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value
	@property
	def telnet(self) -> TelnetConnectParameters:
		return TelnetConnectParameters(self._instance.Telnet)
	@telnet.setter
	def telnet(self, value: TelnetConnectParameters):
		self._instance.Telnet = value
	@property
	def ftp(self) -> FtpConnectParameters:
		return FtpConnectParameters(self._instance.Ftp)
	@ftp.setter
	def ftp(self, value: FtpConnectParameters):
		self._instance.Ftp = value
	@property
	def snpx(self) -> SnpxConnectParameters:
		return SnpxConnectParameters(self._instance.Snpx)
	@snpx.setter
	def snpx(self, value: SnpxConnectParameters):
		self._instance.Snpx = value
	@property
	def rmi(self) -> RmiConnectParameters:
		return RmiConnectParameters(self._instance.Rmi)
	@rmi.setter
	def rmi(self, value: RmiConnectParameters):
		self._instance.Rmi = value
