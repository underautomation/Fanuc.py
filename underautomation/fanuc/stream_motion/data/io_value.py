from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.data.io_type import IOType
from UnderAutomation.Fanuc.StreamMotion.Data import IOValue as io_value
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class IOValue:
	'''State of 16 consecutive I/O read by Stream Motion'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_value()
		else:
			self._instance = _internal

	def get_state(self, index: int) -> bool:
		'''Returns the state of one I/O of the range

		:param index: I/O index, between index and index + 15
		'''
		return self._instance.GetState(index)

	@property
	def type(self) -> IOType:
		'''I/O type'''
		return IOType(int(self._instance.Type))

	@property
	def index(self) -> int:
		'''Index of the first I/O of the range'''
		return self._instance.Index

	@property
	def value(self) -> int:
		'''State of the 16 I/O. Bit 0 is the I/O at index.'''
		return self._instance.Value

	@property
	def age(self) -> int:
		'''Number of status received since this value was read. -1 if it was never read.'''
		return self._instance.Age

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Number of I/O read in one range
IOValue.RangeSize = io_value.RangeSize
