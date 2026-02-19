import typing
from underautomation.fanuc.stream_motion.data.data_style import DataStyle
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
from underautomation.fanuc.stream_motion.data.io_type import IOType
from UnderAutomation.Fanuc.StreamMotion.Data import CommandPacket as command_packet
from UnderAutomation.Fanuc.StreamMotion.Data import DataStyle as data_style
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class CommandPacket:
	'''Command packet to send motion commands to the robot'''
	def __init__(self, dataStyle: DataStyle, motionData: MotionData, _internal = 0):
		'''Constructor with motion data'''
		if(_internal == 0):
			self._instance = command_packet(dataStyle, motionData)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def is_last_data(self) -> bool:
		'''Whether this is the last command data packet'''
		return self._instance.IsLastData

	@is_last_data.setter
	def is_last_data(self, value: bool):
		self._instance.IsLastData = value

	@property
	def read_io_type(self) -> IOType:
		'''Type of I/O to read'''
		return IOType(int(self._instance.ReadIOType))

	@read_io_type.setter
	def read_io_type(self, value: IOType):
		self._instance.ReadIOType = io_type(int(value))

	@property
	def read_io_index(self) -> int:
		'''Index of I/O to read'''
		return self._instance.ReadIOIndex

	@read_io_index.setter
	def read_io_index(self, value: int):
		self._instance.ReadIOIndex = value

	@property
	def read_io_mask(self) -> int:
		'''Mask for I/O read operation'''
		return self._instance.ReadIOMask

	@read_io_mask.setter
	def read_io_mask(self, value: int):
		self._instance.ReadIOMask = value

	@property
	def data_style(self) -> DataStyle:
		'''Data style (Cartesian or Joint)'''
		return DataStyle(int(self._instance.DataStyle))

	@data_style.setter
	def data_style(self, value: DataStyle):
		self._instance.DataStyle = data_style(int(value))

	@property
	def write_io_type(self) -> IOType:
		'''Type of I/O to write'''
		return IOType(int(self._instance.WriteIOType))

	@write_io_type.setter
	def write_io_type(self, value: IOType):
		self._instance.WriteIOType = io_type(int(value))

	@property
	def write_io_index(self) -> int:
		'''Index of I/O to write'''
		return self._instance.WriteIOIndex

	@write_io_index.setter
	def write_io_index(self, value: int):
		self._instance.WriteIOIndex = value

	@property
	def write_io_mask(self) -> int:
		'''Mask for I/O write operation'''
		return self._instance.WriteIOMask

	@write_io_mask.setter
	def write_io_mask(self, value: int):
		self._instance.WriteIOMask = value

	@property
	def write_io_value(self) -> int:
		'''Value to write to I/O'''
		return self._instance.WriteIOValue

	@write_io_value.setter
	def write_io_value(self, value: int):
		self._instance.WriteIOValue = value

	@property
	def motion_data(self) -> MotionData:
		'''Motion data (position values)'''
		return MotionData(None, self._instance.MotionData)

	@motion_data.setter
	def motion_data(self, value: MotionData):
		self._instance.MotionData = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommandPacket):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
