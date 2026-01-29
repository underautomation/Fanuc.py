import typing
from underautomation.fanuc.stream_motion.data.packet_type_from_robot import PacketTypeFromRobot
from underautomation.fanuc.stream_motion.data.robot_status import RobotStatus
from underautomation.fanuc.stream_motion.data.io_read_result import IOReadResult
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import StatePacket as state_packet

class StatePacket:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = state_packet()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def received_at_ticks(self) -> int:
		return self._instance.ReceivedAtTicks
	@property
	def received_at(self) -> typing.Any:
		return self._instance.ReceivedAt
	@property
	def packet_type(self) -> PacketTypeFromRobot:
		return PacketTypeFromRobot(self._instance.PacketType)
	@property
	def version_number(self) -> int:
		return self._instance.VersionNumber
	@property
	def sequence_number(self) -> int:
		return self._instance.SequenceNumber
	@property
	def status(self) -> RobotStatus:
		return RobotStatus(self._instance.Status)
	@property
	def io_read(self) -> IOReadResult:
		return IOReadResult(self._instance.IORead)
	@property
	def time_stamp(self) -> int:
		return self._instance.TimeStamp
	@property
	def cartesian_position(self) -> MotionData:
		return MotionData(None, self._instance.CartesianPosition)
	@property
	def joint_position(self) -> MotionData:
		return MotionData(None, self._instance.JointPosition)
	@property
	def motor_currents(self) -> MotionData:
		return MotionData(None, self._instance.MotorCurrents)
