import typing
from underautomation.fanuc.stream_motion.data.state_packet import StatePacket
from underautomation.fanuc.stream_motion.data.command_packet import CommandPacket
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.fanuc.stream_motion.data.ack_packet import AckPacket
from underautomation.fanuc.stream_motion.data.threshold_type import ThresholdType
from underautomation.fanuc.stream_motion.data.state_received_event_args import StateReceivedEventArgs
from underautomation.fanuc.stream_motion.data.receive_error_event_args import ReceiveErrorEventArgs
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionClientBase as stream_motion_client_base
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class StreamMotionClientBase:
	'''Base class for Stream Motion client (J519 option) Provides UDP-based real-time streaming motion control. The robot sends state packets continuously at high frequency (~500Hz). Commands should be sent in response to StateReceived events using the sequence number from the received state.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the Stream Motion client'''
		if(_internal == 0):
			self._instance = stream_motion_client_base()
		else:
			self._instance = _internal

	def state_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.StateReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def receive_error(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ReceiveError+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))

	def disconnect(self) -> None:
		'''Disconnect from the robot'''
		self._instance.Disconnect()

	def start(self) -> None:
		'''Start streaming motion. This starts a background thread that continuously receives state packets and raises the StateReceived event for each packet.'''
		self._instance.Start()

	def stop(self) -> None:
		'''Stop streaming motion'''
		self._instance.Stop()

	def send_command(self, command: CommandPacket) -> None:
		'''Queue a motion command to be sent with the next state packet's sequence number. The command will be sent automatically when the next state packet is received. It is recommended to call this method within the StateReceived event handler.

		:param command: Command packet to send
		'''
		self._instance.SendCommand(command._instance if command else None)

	def send_joint_command(self, jointPositions: MotionData, readIOType: IOType, readIOIndex: int, readIOMask: int, isLastData: bool=False) -> None:
		'''Queue a joint motion command with I/O read'''
		self._instance.SendJointCommand(jointPositions._instance if jointPositions else None, io_type(int(readIOType)), readIOIndex, readIOMask, isLastData)

	def send_cartesian_command(self, cartesianPosition: MotionData, isLastData: bool=False) -> None:
		'''Queue a Cartesian motion command'''
		self._instance.SendCartesianCommand(cartesianPosition._instance if cartesianPosition else None, isLastData)

	def request_threshold(self, axisNumber: int, thresholdType: ThresholdType) -> AckPacket:
		'''Request threshold data for an axis. Note: This is a synchronous blocking call that should not be called during active streaming.

		:param axisNumber: Axis number (1-9)
		:param thresholdType: Type of threshold to request
		:returns: Acknowledgment packet with threshold data
		'''
		return AckPacket(self._instance.RequestThreshold(axisNumber, threshold_type(int(thresholdType))))

	@property
	def ip(self) -> str:
		'''IP address of the robot'''
		return self._instance.Ip

	@property
	def port(self) -> int:
		'''UDP port used for communication'''
		return self._instance.Port

	@property
	def connected(self) -> bool:
		'''Indicates whether the client is connected'''
		return self._instance.Connected

	@property
	def is_connected(self) -> bool:
		'''Indicates whether the client is connected (alias for Connected)'''
		return self._instance.IsConnected

	@property
	def is_streaming(self) -> bool:
		'''Indicates whether streaming is currently active'''
		return self._instance.IsStreaming

	@property
	def last_state(self) -> StatePacket:
		'''Last received state packet'''
		return StatePacket(self._instance.LastState)

	@property
	def send_timeout_ms(self) -> int:
		'''Send timeout in milliseconds'''
		return self._instance.SendTimeoutMs

	@property
	def receive_timeout_ms(self) -> int:
		'''Receive timeout in milliseconds'''
		return self._instance.ReceiveTimeoutMs

	@property
	def robot_frequency(self) -> float:
		'''Frequency based on robot timestamp (Hz). Calculated from consecutive packet timestamps.'''
		return self._instance.RobotFrequency

	@property
	def measured_frequency(self) -> float:
		'''Measured frequency based on PC receive time (Hz). Actual rate at which packets arrive.'''
		return self._instance.MeasuredFrequency

	@property
	def packet_count(self) -> int:
		'''Total number of state packets received since streaming started'''
		return self._instance.PacketCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
