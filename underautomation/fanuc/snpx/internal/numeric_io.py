import typing
from underautomation.fanuc.snpx.internal.segment_selector import SegmentSelector
from underautomation.fanuc.snpx.internal.segment_offset import SegmentOffset
from underautomation.fanuc.snpx.internal.segment_name import SegmentName
from underautomation.fanuc.snpx.internal.snpx_elements_2 import SnpxElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import NumericIO as numeric_io

class NumericIO(SnpxElements2[int, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_io()
		else:
			self._instance = _internal
	def read(self, firstIndex: int, count: int) -> typing.List[int]:
		return self._instance.Read(firstIndex, count)
	def write(self, firstIndex: int, values: typing.List[int]) -> None:
		self._instance.Write(firstIndex, values)
	@property
	def segment_selector(self) -> SegmentSelector:
		return SegmentSelector(self._instance.SegmentSelector)
	@property
	def segment_offset(self) -> SegmentOffset:
		return SegmentOffset(self._instance.SegmentOffset)
	@property
	def segment_name(self) -> SegmentName:
		return SegmentName(self._instance.SegmentName)
