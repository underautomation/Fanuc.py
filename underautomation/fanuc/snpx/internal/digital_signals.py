from __future__ import annotations
import typing
from underautomation.fanuc.snpx.internal.segment_selector import SegmentSelector
from underautomation.fanuc.snpx.internal.segment_offset import SegmentOffset
from underautomation.fanuc.snpx.internal.segment_name import SegmentName
from underautomation.fanuc.snpx.internal.snpx_elements_2 import SnpxElements2
from UnderAutomation.Fanuc.Snpx.Internal import DigitalSignals as digital_signals
from UnderAutomation.Fanuc.Snpx.Internal import SegmentSelector as segment_selector
from UnderAutomation.Fanuc.Snpx.Internal import SegmentOffset as segment_offset
from UnderAutomation.Fanuc.Snpx.Internal import SegmentName as segment_name

class DigitalSignals(SnpxElements2[bool, int]):
	'''Provides read/write access to digital I/O signals on the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = digital_signals()
		else:
			self._instance = _internal

	@typing.overload
	def read(self, firstIndex: int, count: int) -> typing.List[bool]: ...

	@typing.overload
	def read(self, index: int) -> bool: ...

	def read(self, *args, **kwargs) -> typing.List[bool] | bool:
		'''Reads a range of digital signals.
		Reads the digital signal at the specified index.

		Arguments: (firstIndex, count)
		Arguments: (index)
		:param firstIndex: The first signal index (1-based).
		:param count: The number of signals to read.
		:param index: The signal index (1-based).
		:returns: An array of boolean signal states.
		'''
		__a = _bind_overload(args, kwargs, ['firstIndex', 'count'], {})
		if __a is not None:
			firstIndex, count = __a
			return self._instance.Read(firstIndex, count)
		__a = _bind_overload(args, kwargs, ['index'], {})
		if __a is not None:
			index, = __a
			return self._instance.Read(index)
		raise TypeError("read(): no overload takes these arguments")

	def write(self, firstIndex_or_index: int, value_or_values: bool | typing.List[bool]) -> None:
		'''Writes a value to the digital signal at the specified index.
		Writes values to consecutive digital signals.

		:param firstIndex_or_index: The signal index (1-based). Or: The first signal index (1-based).
		:param value_or_values: The boolean value to write. Or: The boolean values to write.
		'''
		self._instance.Write(firstIndex_or_index, value_or_values)

	@property
	def segment_selector(self) -> SegmentSelector:
		'''Gets the segment selector for this signal group.'''
		return SegmentSelector(int(self._instance.SegmentSelector))

	@property
	def segment_offset(self) -> SegmentOffset:
		'''Gets the segment offset for this signal group.'''
		return SegmentOffset(int(self._instance.SegmentOffset))

	@property
	def segment_name(self) -> SegmentName:
		'''Gets the segment name identifying this signal group.'''
		return SegmentName(int(self._instance.SegmentName))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DigitalSignals):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
