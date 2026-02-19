import typing
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
from UnderAutomation.Fanuc.Snpx.Assignment import PositionRegistersBatchAssignment as position_registers_batch_assignment

class PositionRegistersBatchAssignment(BatchAssignment2[Position, int]):
	'''Batch assignment for reading multiple position registers at once.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PositionRegistersBatchAssignment class.'''
		if(_internal == 0):
			self._instance = position_registers_batch_assignment()
		else:
			self._instance = _internal

	def read(self) -> typing.List[Position]:
		'''Reads all position registers assigned in this batch.

		:returns: An array of Position values.
		'''
		return [Position(None, None, None, None, x) for x in self._instance.Read()]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PositionRegistersBatchAssignment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
