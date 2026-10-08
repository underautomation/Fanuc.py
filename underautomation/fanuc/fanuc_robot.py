from __future__ import annotations
import typing
from underautomation.fanuc.connection_parameters import ConnectionParameters
from underautomation.fanuc.telnet.internal.telnet_client_internal import TelnetClientInternal
from underautomation.fanuc.ftp.internal.ftp_client_internal import FtpClientInternal
from underautomation.fanuc.snpx.internal.snpx_client_internal import SnpxClientInternal
from underautomation.fanuc.rmi.internal.rmi_client_internal import RmiClientInternal
from underautomation.fanuc.stream_motion.internal.stream_motion_client_internal import StreamMotionClientInternal
from underautomation.fanuc.cgtp.internal.cgtp_client_internal import CgtpClientInternal
from underautomation.fanuc.license.license_info import LicenseInfo
from UnderAutomation.Fanuc import FanucRobot as fanuc_robot

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class FanucRobot:
	'''Main class of the SDK that represents a connection to a Fanuc robot'''
	def __init__(self, _internal = 0):
		'''Instanciate a new Fanuc robot connection'''
		if(_internal == 0):
			self._instance = fanuc_robot()
		else:
			self._instance = _internal

	def connect(self, ip_or_parameters: str | ConnectionParameters) -> None:
		'''Connect to robot by IP with default connection parameters
		Initialize a conenction to the robot with specified parameters
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

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
		__r = fanuc_robot.RegisterLicense(licensee, key)
		return None if __r is None else LicenseInfo(None, None, __r)

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
		__r = self._instance.Telnet
		return None if __r is None else TelnetClientInternal(__r)

	@property
	def ftp(self) -> FtpClientInternal:
		'''FTP client for memory and file access'''
		__r = self._instance.Ftp
		return None if __r is None else FtpClientInternal(__r)

	@property
	def snpx(self) -> SnpxClientInternal:
		'''SNPX client for IO, alarms and task reading'''
		__r = self._instance.Snpx
		return None if __r is None else SnpxClientInternal(__r)

	@property
	def rmi(self) -> RmiClientInternal:
		'''RMI client for remote motion interface'''
		__r = self._instance.Rmi
		return None if __r is None else RmiClientInternal(__r)

	@property
	def stream_motion(self) -> StreamMotionClientInternal:
		'''Stream Motion client for real-time motion control'''
		__r = self._instance.StreamMotion
		return None if __r is None else StreamMotionClientInternal(__r)

	@property
	def cgtp(self) -> CgtpClientInternal:
		'''CGTP Web Server client for HTTP-based COMET RPC interface'''
		__r = self._instance.Cgtp
		return None if __r is None else CgtpClientInternal(__r)

	@staticmethod
	def _get_license_info() -> LicenseInfo:
		'''Return information about your license'''
		__r = fanuc_robot.LicenseInfo
		return None if __r is None else LicenseInfo(None, None, __r)

	license_info = _StaticProperty(_get_license_info)
	del _get_license_info

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
