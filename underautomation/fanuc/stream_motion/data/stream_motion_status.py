from __future__ import annotations
import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.fanuc.stream_motion.data.io_type import IOType
from UnderAutomation.Fanuc.StreamMotion.Data import StreamMotionStatus as stream_motion_status
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class StreamMotionStatus:
	'''Status sent by the robot every communication cycle'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_status()
		else:
			self._instance = _internal

	@property
	def sequence_number(self) -> int:
		'''Sequence number of this status. It starts at 1 when the status output starts.'''
		return self._instance.SequenceNumber

	@property
	def timestamp(self) -> int:
		'''Time stamp of the robot when the position and the motor currents were read, in ms (resolution 2 ms)'''
		return self._instance.Timestamp

	@property
	def raw_status(self) -> int:
		'''Raw status byte'''
		return self._instance.RawStatus

	@property
	def is_waiting_for_command(self) -> bool:
		'''The robot executes an IBGN start instruction and waits for positions'''
		return self._instance.IsWaitingForCommand

	@property
	def is_command_received(self) -> bool:
		'''The robot received at least one position during the current IBGN start instruction'''
		return self._instance.IsCommandReceived

	@property
	def is_system_ready(self) -> bool:
		'''System ready (SYSRDY) is ON'''
		return self._instance.IsSystemReady

	@property
	def is_moving(self) -> bool:
		'''The robot is moving'''
		return self._instance.IsMoving

	@property
	def output_divider(self) -> int:
		'''With protocol version 3 or later, the robot sends a status once every n communication cycles when it slows down by itself, and this value is n. It is 1 in normal operation and with older protocol versions.'''
		return self._instance.OutputDivider

	@property
	def joint_position(self) -> JointsPosition:
		'''Current joint position of the robot (servo position), in degrees (mm for linear axes)'''
		__r = self._instance.JointPosition
		return None if __r is None else JointsPosition(None, None, None, None, None, None, None, None, None, __r)

	@property
	def cartesian_position(self) -> ExtendedCartesianPosition:
		'''Current Cartesian position of the robot (servo position) in the world frame, with extended axes. It is the flange center, or the tool center point when the system variable $STMO.$STAT_US_TCP is TRUE.'''
		__r = self._instance.CartesianPosition
		return None if __r is None else ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, __r)

	@property
	def motor_currents(self) -> typing.List[float]:
		'''Motor current of each axis, in A (9 values)'''
		return self._instance.MotorCurrents

	@property
	def read_io_type(self) -> IOType:
		'''Type of the I/O read in this status'''
		return IOType(int(self._instance.ReadIOType))

	@property
	def read_io_index(self) -> int:
		'''Index of the first I/O read in this status'''
		return self._instance.ReadIOIndex

	@property
	def read_io_mask(self) -> int:
		'''Mask of the I/O read in this status'''
		return self._instance.ReadIOMask

	@property
	def read_io_value(self) -> int:
		'''State of the 16 I/O read in this status. Bit 0 is the I/O at read_io_index.'''
		return self._instance.ReadIOValue

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
