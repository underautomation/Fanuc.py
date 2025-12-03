import typing
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.telnet.internal.telnet_client_internal import TelnetClientInternal
from underautomation.fanuc.ftp.internal.ftp_client_internal import FtpClientInternal
from underautomation.fanuc.snpx.internal.snpx_client_internal import SnpxClientInternal
from underautomation.fanuc.rmi.internal.rmi_client_internal import RmiClientInternal
from underautomation.fanuc.license.license_info import LicenseInfo
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__),  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc import FanucRobot as fanuc_robot

class FanucRobot:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fanuc_robot()
		else:
			self._instance = _internal
	def connect(self, parameters: ConnectionParameters) -> None:
		self._instance.Connect(parameters._instance if parameters else None)
	def disconnect(self) -> None:
		self._instance.Disconnect()
	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		return LicenseInfo(None, None, fanuc_robot.RegisterLicense(licensee, key))
	@property
	def address(self) -> str:
		return self._instance.Address
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def telnet(self) -> TelnetClientInternal:
		return TelnetClientInternal(self._instance.Telnet)
	@property
	def ftp(self) -> FtpClientInternal:
		return FtpClientInternal(self._instance.Ftp)
	@property
	def snpx(self) -> SnpxClientInternal:
		return SnpxClientInternal(self._instance.Snpx)
	@property
	def rmi(self) -> RmiClientInternal:
		return RmiClientInternal(self._instance.Rmi)
	@property
	def license_info(self) -> LicenseInfo:
		return LicenseInfo(None, None, self._instance.LicenseInfo)
