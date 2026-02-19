import typing
from datetime import datetime, timedelta
from underautomation.fanuc.stream_motion.data.packet_type_from_robot import PacketTypeFromRobot
from underautomation.fanuc.stream_motion.data.robot_status import RobotStatus
from underautomation.fanuc.stream_motion.data.io_read_result import IOReadResult
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
from UnderAutomation.Fanuc.StreamMotion.Data import StatePacket as state_packet
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeFromRobot as packet_type_from_robot

class StatePacket:
	'''State packet received from the robot containing current position, status, and motor currents'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = state_packet()
		else:
			self._instance = _internal

	@property
	def received_at_ticks(self) -> int:
		'''Time when this packet was received on the PC (UTC ticks)'''
		return self._instance.ReceivedAtTicks

	@property
	def received_at(self) -> datetime:
		'''Time when this packet was received on the PC'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.ReceivedAt.Ticks // 10)

	@property
	def packet_type(self) -> PacketTypeFromRobot:
		'''Packet type (always State=0)'''
		return PacketTypeFromRobot(int(self._instance.PacketType))

	@property
	def version_number(self) -> int:
		'''Protocol version number'''
		return self._instance.VersionNumber

	@property
	def sequence_number(self) -> int:
		'''Sequence number for packet tracking'''
		return self._instance.SequenceNumber

	@property
	def status(self) -> RobotStatus:
		'''Robot status flags'''
		return RobotStatus(self._instance.Status)

	@property
	def io_read(self) -> IOReadResult:
		'''Result of I/O read operation'''
		return IOReadResult(self._instance.IORead)

	@property
	def time_stamp(self) -> int:
		'''Time stamp when position data and motor current are recorded (ms, resolution 2ms)'''
		return self._instance.TimeStamp

	@property
	def cartesian_position(self) -> MotionData:
		'''Current Cartesian position (world to tool0)'''
		return MotionData(None, self._instance.CartesianPosition)

	@property
	def joint_position(self) -> MotionData:
		'''Current joint position'''
		return MotionData(None, self._instance.JointPosition)

	@property
	def motor_currents(self) -> MotionData:
		'''Current motor currents (Amperes)'''
		return MotionData(None, self._instance.MotorCurrents)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StatePacket):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
