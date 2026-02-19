import typing
from underautomation.fanuc.snpx.assignment.flag_batch_assignment import FlagBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import Flags as flags

class Flags(SnpxWritableAssignableIndexableElements2[bool, FlagBatchAssignment]):
	'''Provides access to flag registers (F[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flags()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> FlagBatchAssignment:
		'''Creates a batch assignment for reading multiple flags.

		:param startIndex: The starting flag index.
		:param count: The number of consecutive flags.
		:returns: A batch assignment for the specified range.
		'''
		return FlagBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Flags):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
