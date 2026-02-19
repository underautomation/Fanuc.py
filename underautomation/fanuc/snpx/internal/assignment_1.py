import typing
from underautomation.fanuc.snpx.internal.assignment import Assignment
from UnderAutomation.Fanuc.Snpx.Internal import Assignment as assignment_1

TIndex = typing.TypeVar('TIndex')
class Assignment1(Assignment, typing.Generic[TIndex]):
	'''Represents a typed SNPX memory assignment with an index.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = assignment_1()
		else:
			self._instance = _internal

	@property
	def index(self) -> TIndex:
		'''Gets the index of this assignment.'''
		return self._instance.Index

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Assignment1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
