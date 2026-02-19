import typing
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.common.telnet_connect_parameters import TelnetConnectParameters
from underautomation.fanuc.common.ftp_connect_parameters import FtpConnectParameters
from underautomation.fanuc.common.snpx_connect_parameters import SnpxConnectParameters
from underautomation.fanuc.common.rmi_connect_parameters import RmiConnectParameters
from underautomation.fanuc.common.stream_motion_connect_parameters import StreamMotionConnectParameters
from UnderAutomation.Fanuc import ConnectionParameters as connection_parameters
from UnderAutomation.Fanuc.Common import Languages as languages

class ConnectionParameters:
	'''Connection parameters'''
	def __init__(self, address: str, _internal = 0):
		'''Instanciate a new connection parameters with a specified address'''
		if(_internal == 0):
			self._instance = connection_parameters(address)
		else:
			self._instance = _internal

	@property
	def address(self) -> str:
		'''Address of the robot (IP, host name, or path to ROBOGUIDE project folder)'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def ping_before_connect(self) -> bool:
		'''Send a ping command before initializing any connections'''
		return self._instance.PingBeforeConnect

	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value

	@property
	def language(self) -> Languages:
		'''Controller language (default: English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def telnet(self) -> TelnetConnectParameters:
		'''Sends commands to the robot for remote control'''
		return TelnetConnectParameters(self._instance.Telnet)

	@telnet.setter
	def telnet(self, value: TelnetConnectParameters):
		self._instance.Telnet = value._instance if value else None

	@property
	def ftp(self) -> FtpConnectParameters:
		'''Access controller internal memory to read variables, IO, positions, diagnosis, ...'''
		return FtpConnectParameters(self._instance.Ftp)

	@ftp.setter
	def ftp(self, value: FtpConnectParameters):
		self._instance.Ftp = value._instance if value else None

	@property
	def snpx(self) -> SnpxConnectParameters:
		'''Read and write IOs, read and clear alarms, read current program tasks'''
		return SnpxConnectParameters(self._instance.Snpx)

	@snpx.setter
	def snpx(self, value: SnpxConnectParameters):
		self._instance.Snpx = value._instance if value else None

	@property
	def rmi(self) -> RmiConnectParameters:
		'''Parameters for RMI (Remote Motion Interface)'''
		return RmiConnectParameters(self._instance.Rmi)

	@rmi.setter
	def rmi(self, value: RmiConnectParameters):
		self._instance.Rmi = value._instance if value else None

	@property
	def stream_motion(self) -> StreamMotionConnectParameters:
		'''Parameters for Stream Motion (J519 option) - real-time streaming motion control over UDP'''
		return StreamMotionConnectParameters(self._instance.StreamMotion)

	@stream_motion.setter
	def stream_motion(self, value: StreamMotionConnectParameters):
		self._instance.StreamMotion = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectionParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
