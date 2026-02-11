import typing
from underautomation.fanuc.stream_motion.data.data_style import DataStyle
from underautomation.fanuc.stream_motion.data.motion_data import MotionData
from underautomation.fanuc.stream_motion.data.io_type import IOType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import CommandPacket as command_packet
from UnderAutomation.Fanuc.StreamMotion.Data import DataStyle as data_style
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class CommandPacket:
	def __init__(self, dataStyle: DataStyle, motionData: MotionData, _internal = 0):
		if(_internal == 0):
			self._instance = command_packet(dataStyle, motionData)
		else:
			self._instance = _internal
	@property
	def is_last_data(self) -> bool:
		return self._instance.IsLastData
	@is_last_data.setter
	def is_last_data(self, value: bool):
		self._instance.IsLastData = value
	@property
	def read_io_type(self) -> IOType:
		return IOType(self._instance.ReadIOType)
	@read_io_type.setter
	def read_io_type(self, value: IOType):
		self._instance.ReadIOType = io_type(int(value))
	@property
	def read_io_index(self) -> int:
		return self._instance.ReadIOIndex
	@read_io_index.setter
	def read_io_index(self, value: int):
		self._instance.ReadIOIndex = value
	@property
	def read_io_mask(self) -> int:
		return self._instance.ReadIOMask
	@read_io_mask.setter
	def read_io_mask(self, value: int):
		self._instance.ReadIOMask = value
	@property
	def data_style(self) -> DataStyle:
		return DataStyle(self._instance.DataStyle)
	@data_style.setter
	def data_style(self, value: DataStyle):
		self._instance.DataStyle = data_style(int(value))
	@property
	def write_io_type(self) -> IOType:
		return IOType(self._instance.WriteIOType)
	@write_io_type.setter
	def write_io_type(self, value: IOType):
		self._instance.WriteIOType = io_type(int(value))
	@property
	def write_io_index(self) -> int:
		return self._instance.WriteIOIndex
	@write_io_index.setter
	def write_io_index(self, value: int):
		self._instance.WriteIOIndex = value
	@property
	def write_io_mask(self) -> int:
		return self._instance.WriteIOMask
	@write_io_mask.setter
	def write_io_mask(self, value: int):
		self._instance.WriteIOMask = value
	@property
	def write_io_value(self) -> int:
		return self._instance.WriteIOValue
	@write_io_value.setter
	def write_io_value(self, value: int):
		self._instance.WriteIOValue = value
	@property
	def motion_data(self) -> MotionData:
		return MotionData(None, self._instance.MotionData)
	@motion_data.setter
	def motion_data(self, value: MotionData):
		self._instance.MotionData = value
