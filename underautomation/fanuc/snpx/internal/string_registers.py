import typing
from underautomation.fanuc.snpx.assignment.string_registers_batch_assignment import StringRegistersBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import StringRegisters as string_registers

class StringRegisters(SnpxWritableAssignableIndexableElements2[str, StringRegistersBatchAssignment]):
	'''Provides access to string registers (SR[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_registers()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> StringRegistersBatchAssignment:
		'''Creates a batch assignment for reading multiple string registers.

		:param startIndex: The starting register index.
		:param count: The number of consecutive registers.
		:returns: A batch assignment for the specified range.
		'''
		return StringRegistersBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringRegisters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
