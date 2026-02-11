import typing
from underautomation.fanuc.stream_motion.data.state_packet import StatePacket
from underautomation.fanuc.stream_motion.data.command_packet import CommandPacket
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.fanuc.stream_motion.data.ack_packet import AckPacket
from underautomation.fanuc.stream_motion.data.threshold_type import ThresholdType
from underautomation.fanuc.stream_motion.data.state_received_event_args import StateReceivedEventArgs
from underautomation.fanuc.stream_motion.data.receive_error_event_args import ReceiveErrorEventArgs
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionClientBase as stream_motion_client_base
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class StreamMotionClientBase:
	def __init__(self, _internal = 0):
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
		self._instance.Disconnect()
	def start(self) -> None:
		self._instance.Start()
	def stop(self) -> None:
		self._instance.Stop()
	def send_command(self, command: CommandPacket) -> None:
		self._instance.SendCommand(command._instance if command else None)
	def send_joint_command(self, jointPositions: MotionData, readIOType: IOType, readIOIndex: int, readIOMask: int, isLastData: bool=False) -> None:
		self._instance.SendJointCommand(jointPositions._instance if jointPositions else None, io_type(int(readIOType)), readIOIndex, readIOMask, isLastData)
	def send_cartesian_command(self, cartesianPosition: MotionData, isLastData: bool=False) -> None:
		self._instance.SendCartesianCommand(cartesianPosition._instance if cartesianPosition else None, isLastData)
	def request_threshold(self, axisNumber: int, thresholdType: ThresholdType) -> AckPacket:
		return AckPacket(self._instance.RequestThreshold(axisNumber, threshold_type(int(thresholdType))))
	@property
	def ip(self) -> str:
		return self._instance.Ip
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def connected(self) -> bool:
		return self._instance.Connected
	@property
	def is_connected(self) -> bool:
		return self._instance.IsConnected
	@property
	def is_streaming(self) -> bool:
		return self._instance.IsStreaming
	@property
	def last_state(self) -> StatePacket:
		return StatePacket(self._instance.LastState)
	@property
	def send_timeout_ms(self) -> int:
		return self._instance.SendTimeoutMs
	@property
	def receive_timeout_ms(self) -> int:
		return self._instance.ReceiveTimeoutMs
	@property
	def robot_frequency(self) -> float:
		return self._instance.RobotFrequency
	@property
	def measured_frequency(self) -> float:
		return self._instance.MeasuredFrequency
	@property
	def packet_count(self) -> int:
		return self._instance.PacketCount
