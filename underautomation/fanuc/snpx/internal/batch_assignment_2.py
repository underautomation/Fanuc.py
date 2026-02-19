import typing
from underautomation.fanuc.snpx.internal.assignment_1 import Assignment1
from UnderAutomation.Fanuc.Snpx.Internal import BatchAssignment as batch_assignment_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class BatchAssignment2(typing.Generic[TValue, TIndex]):
	'''Abstract base class for batch assignment operations that read multiple values at once.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = batch_assignment_2()
		else:
			self._instance = _internal

	def read(self) -> typing.List[TValue]:
		'''Reads all values from the batch assignment.

		:returns: An array of values read from the robot.
		'''
		return list(self._instance.Read())

	@property
	def assignments(self) -> typing.List[Assignment1]:
		'''The assignments included in this batch.'''
		return [Assignment1(x) for x in self._instance.Assignments]

	@assignments.setter
	def assignments(self, value: typing.List[Assignment1]):
		self._instance.Assignments = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BatchAssignment2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
