import typing
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.telnet.internal.telnet_client_internal import TelnetClientInternal
from underautomation.fanuc.ftp.internal.ftp_client_internal import FtpClientInternal
from underautomation.fanuc.snpx.internal.snpx_client_internal import SnpxClientInternal
from underautomation.fanuc.rmi.internal.rmi_client_internal import RmiClientInternal
from underautomation.fanuc.stream_motion.internal.stream_motion_client_internal import StreamMotionClientInternal
from underautomation.fanuc.license.license_info import LicenseInfo
from UnderAutomation.Fanuc import FanucRobot as fanuc_robot

class FanucRobot:
	'''Main class of the SDK that represents a connection to a Fanuc robot'''
	def __init__(self, _internal = 0):
		'''Instanciate a new Fanuc robot connection'''
		if(_internal == 0):
			self._instance = fanuc_robot()
		else:
			self._instance = _internal

	def connect(self, parameters: ConnectionParameters) -> None:
		'''Initialize a conenction to the robot with specified parameters'''
		self._instance.Connect(parameters._instance if parameters else None)

	def disconnect(self) -> None:
		'''Disconnect all services connected to the robot'''
		self._instance.Disconnect()

	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		'''If you have a license And a key, please call this static method to register the product And exit the trial period ou can register a product even if the trial period has ended

		:param licensee: Your organization name
		:param key: The associated key supplied by UnderAutomation
		:returns: Information about the supplied license
		'''
		return LicenseInfo(None, None, fanuc_robot.RegisterLicense(licensee, key))

	@property
	def address(self) -> str:
		'''IP or robot name'''
		return self._instance.Address

	@property
	def enabled(self) -> bool:
		'''Indicates whether any service is currently connected to the robot'''
		return self._instance.Enabled

	@property
	def telnet(self) -> TelnetClientInternal:
		'''Telnet client for remote command execution'''
		return TelnetClientInternal(self._instance.Telnet)

	@property
	def ftp(self) -> FtpClientInternal:
		'''FTP client for memory and file access'''
		return FtpClientInternal(self._instance.Ftp)

	@property
	def snpx(self) -> SnpxClientInternal:
		'''SNPX client for IO, alarms and task reading'''
		return SnpxClientInternal(self._instance.Snpx)

	@property
	def rmi(self) -> RmiClientInternal:
		'''RMI client for remote motion interface'''
		return RmiClientInternal(self._instance.Rmi)

	@property
	def stream_motion(self) -> StreamMotionClientInternal:
		'''Stream Motion client for real-time motion control'''
		return StreamMotionClientInternal(self._instance.StreamMotion)

	@property
	def license_info(self) -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FanucRobot):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
