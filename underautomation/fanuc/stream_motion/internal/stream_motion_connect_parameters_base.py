from __future__ import annotations
import typing
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionConnectParametersBase as stream_motion_connect_parameters_base

class StreamMotionConnectParametersBase:
	'''Connection parameters for Stream Motion (J519 option)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def port(self) -> int:
		'''UDP port of the robot for Stream Motion'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def protocol_version(self) -> int:
		'''Protocol version, from 1 to 3. The highest version accepted by a controller is in the system variable $STMO.$USABLE_VER. A higher version raises an alarm on the robot and no status is received. Version 2 sends joint positions in double precision. Version 3 lets the robot send its status less often when it slows down by itself. A version 4 exists on some recent controllers for ROS 2 only. It is not supported.'''
		return self._instance.ProtocolVersion

	@protocol_version.setter
	def protocol_version(self, value: int):
		self._instance.ProtocolVersion = value

	@property
	def buffer_lead_time(self) -> float:
		'''Time of positions sent in advance and kept in the robot buffer, in seconds. It protects against late packets from the PC, but adds the same delay to the motion. It is converted to a number of communication cycles, limited by packet_stack_size minus 2. 0 disables the advance.'''
		return self._instance.BufferLeadTime

	@buffer_lead_time.setter
	def buffer_lead_time(self, value: float):
		self._instance.BufferLeadTime = value

	@property
	def packet_stack_size(self) -> int:
		'''Size of the robot buffer. It must be equal to the system variable $STMO.$PKT_STACK of the robot (2 to 10).'''
		return self._instance.PacketStackSize

	@packet_stack_size.setter
	def packet_stack_size(self, value: int):
		self._instance.PacketStackSize = value

	@property
	def status_timeout_ms(self) -> int:
		'''Maximum time without status from the robot before the connection is considered lost, in milliseconds'''
		return self._instance.StatusTimeoutMs

	@status_timeout_ms.setter
	def status_timeout_ms(self, value: int):
		self._instance.StatusTimeoutMs = value

	@property
	def high_priority(self) -> bool:
		'''Runs the communication thread with a high priority to reduce delays (default: true)'''
		return self._instance.HighPriority

	@high_priority.setter
	def high_priority(self, value: bool):
		self._instance.HighPriority = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default UDP port of the robot for Stream Motion
StreamMotionConnectParametersBase.DEFAULT_PORT = stream_motion_connect_parameters_base.DEFAULT_PORT

# Default protocol version. Version 1 is accepted by all controllers.
StreamMotionConnectParametersBase.DEFAULT_PROTOCOL_VERSION = stream_motion_connect_parameters_base.DEFAULT_PROTOCOL_VERSION

# Default time of positions kept in advance in the robot buffer, in seconds
StreamMotionConnectParametersBase.DEFAULT_BUFFER_LEAD_TIME = stream_motion_connect_parameters_base.DEFAULT_BUFFER_LEAD_TIME

# Default size of the robot buffer (default value of the system variable $STMO.$PKT_STACK)
StreamMotionConnectParametersBase.DEFAULT_PACKET_STACK_SIZE = stream_motion_connect_parameters_base.DEFAULT_PACKET_STACK_SIZE

# Default maximum time without status from the robot, in milliseconds
StreamMotionConnectParametersBase.DEFAULT_STATUS_TIMEOUT_MS = stream_motion_connect_parameters_base.DEFAULT_STATUS_TIMEOUT_MS
