import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from UnderAutomation.Fanuc.Snpx.Internal import SnpxWritableAssignableIndexableElements as snpx_writable_assignable_indexable_elements_2

TValue = typing.TypeVar('TValue')
TAssignment = typing.TypeVar('TAssignment')
class SnpxWritableAssignableIndexableElements2(SnpxWritableAssignableElements3[TValue, int, TAssignment], typing.Generic[TValue, TAssignment]):
	'''Abstract base class for writable assignable elements accessed by integer index.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_writable_assignable_indexable_elements_2()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> TAssignment:
		'''Creates a batch assignment for a range of consecutive indices.

		:param startIndex: The starting index.
		:param count: The number of consecutive elements.
		:returns: A batch assignment for the specified range.
		'''
		return self._instance.CreateBatchAssignment(startIndex, count)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxWritableAssignableIndexableElements2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
