import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
from UnderAutomation.Fanuc.Snpx.Assignment import NumericRegistersBatchAssignment as numeric_registers_batch_assignment

class NumericRegistersBatchAssignment(BatchAssignment2[float, int]):
	'''Batch assignment for reading multiple numeric registers at once.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the NumericRegistersBatchAssignment class.'''
		if(_internal == 0):
			self._instance = numeric_registers_batch_assignment()
		else:
			self._instance = _internal

	def read(self) -> typing.List[float]:
		'''Read all numeric registers assigned in this batch assignment.

		:returns: Returns an array of float values representing the numeric registers
		'''
		return self._instance.Read()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericRegistersBatchAssignment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
