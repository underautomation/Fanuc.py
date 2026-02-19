import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from UnderAutomation.Fanuc.Snpx.Internal import SnpxWritableAssignableElements as snpx_writable_assignable_elements_3

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
TAssignment = typing.TypeVar('TAssignment')
class SnpxWritableAssignableElements3(SnpxAssignableElements2[TValue, TIndex], typing.Generic[TValue, TIndex, TAssignment]):
	'''Abstract base class for writable assignable SNPX elements.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_writable_assignable_elements_3()
		else:
			self._instance = _internal

	def write(self, index: TIndex, value: TValue) -> None:
		'''Write value at a certain index.

		:param index: The element index.
		:param value: The value to write.
		'''
		self._instance.Write(index, value)

	def create_batch_assignment(self, indexes: typing.List[TIndex]) -> TAssignment:
		'''Creates a batch assignment for the specified indices.

		:param indexes: The indices to include in the batch.
		:returns: A batch assignment for the specified indices.
		'''
		return self._instance.CreateBatchAssignment(indexes)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxWritableAssignableElements3):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
