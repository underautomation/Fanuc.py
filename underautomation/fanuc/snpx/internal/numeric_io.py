import typing
from underautomation.fanuc.snpx.internal.segment_selector import SegmentSelector
from underautomation.fanuc.snpx.internal.segment_offset import SegmentOffset
from underautomation.fanuc.snpx.internal.segment_name import SegmentName
from underautomation.fanuc.snpx.internal.snpx_elements_2 import SnpxElements2
from UnderAutomation.Fanuc.Snpx.Internal import NumericIO as numeric_io
from UnderAutomation.Fanuc.Snpx.Internal import SegmentSelector as segment_selector
from UnderAutomation.Fanuc.Snpx.Internal import SegmentOffset as segment_offset
from UnderAutomation.Fanuc.Snpx.Internal import SegmentName as segment_name

class NumericIO(SnpxElements2[int, int]):
	'''Provides read/write access to numeric (group/analog) I/O on the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_io()
		else:
			self._instance = _internal

	def read(self, firstIndex: int, count: int) -> typing.List[int]:
		'''Reads a range of numeric I/O values.

		:param firstIndex: The first I/O index (1-based).
		:param count: The number of values to read.
		:returns: An array of numeric I/O values.
		'''
		return self._instance.Read(firstIndex, count)

	def write(self, firstIndex: int, values: typing.List[int]) -> None:
		'''Writes values to consecutive numeric I/O.

		:param firstIndex: The first I/O index (1-based).
		:param values: The values to write.
		'''
		self._instance.Write(firstIndex, values)

	@property
	def segment_selector(self) -> SegmentSelector:
		'''Gets the segment selector for this I/O group.'''
		return SegmentSelector(int(self._instance.SegmentSelector))

	@property
	def segment_offset(self) -> SegmentOffset:
		'''Gets the segment offset for this I/O group.'''
		return SegmentOffset(int(self._instance.SegmentOffset))

	@property
	def segment_name(self) -> SegmentName:
		'''Gets the segment name identifying this I/O group.'''
		return SegmentName(int(self._instance.SegmentName))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericIO):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
