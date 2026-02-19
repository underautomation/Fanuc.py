import typing
from underautomation.fanuc.snpx.assignment.numeric_registers_batch_assignment import NumericRegistersBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import NumericRegisters as numeric_registers

class NumericRegisters(SnpxWritableAssignableIndexableElements2[float, NumericRegistersBatchAssignment]):
	'''Provides access to numeric registers (R[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_registers()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> NumericRegistersBatchAssignment:
		'''Creates a batch assignment for reading multiple numeric registers.

		:param startIndex: The starting register index.
		:param count: The number of consecutive registers.
		:returns: A batch assignment for the specified range.
		'''
		return NumericRegistersBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericRegisters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
