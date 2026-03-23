import typing
from __future__ import annotation
from underautomation.fanuc.snpx.assignment.numeric_registers_int16_batch_assignment import NumericRegistersInt16BatchAssignment
from underautomation.fanuc.snpx.internal.numeric_registers_base_2 import NumericRegistersBase2
from UnderAutomation.Fanuc.Snpx.Internal import NumericRegistersInt16 as numeric_registers_int16

class NumericRegistersInt16(NumericRegistersBase2[int, NumericRegistersInt16BatchAssignment]):
	'''Provides access to numeric registers as 16 bits integer (R[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_registers_int16()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> NumericRegistersInt16BatchAssignment:
		'''Creates a batch assignment for reading multiple numeric registers.

		:param startIndex: The starting register index.
		:param count: The number of consecutive registers.
		:returns: A batch assignment for the specified range.
		'''
		return NumericRegistersInt16BatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericRegistersInt16):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
