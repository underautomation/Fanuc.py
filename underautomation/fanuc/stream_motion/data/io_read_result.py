import typing
from underautomation.fanuc.stream_motion.data.io_type import IOType
from UnderAutomation.Fanuc.StreamMotion.Data import IOReadResult as io_read_result
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class IOReadResult:
	'''Result of an I/O read operation'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_read_result()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def type(self) -> IOType:
		'''Type of I/O that was read'''
		return IOType(int(self._instance.Type))

	@property
	def index(self) -> int:
		'''Index of the I/O'''
		return self._instance.Index

	@property
	def mask(self) -> int:
		'''Mask applied to the read'''
		return self._instance.Mask

	@property
	def value(self) -> int:
		'''Value read from the I/O'''
		return self._instance.Value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOReadResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
