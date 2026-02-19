import typing
from underautomation.fanuc.snpx.internal.assignment_1 import Assignment1
from underautomation.fanuc.snpx.internal.snpx_elements_2 import SnpxElements2
from UnderAutomation.Fanuc.Snpx.Internal import SnpxAssignableElements as snpx_assignable_elements_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class SnpxAssignableElements2(SnpxElements2[TValue, TIndex], typing.Generic[TValue, TIndex]):
	'''Abstract base class for SNPX elements that support memory assignment for efficient access.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_assignable_elements_2()
		else:
			self._instance = _internal

	def read(self, index: TIndex) -> TValue:
		return self._instance.Read(index)

	def get_or_create_assignment(self, index: TIndex) -> Assignment1[TIndex]:
		'''Gets or creates an assignment for the specified index.

		:param index: The index to get or create an assignment for.
		:returns: The existing or newly created assignment.
		'''
		return Assignment1[TIndex](self._instance.GetOrCreateAssignment(index))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxAssignableElements2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
