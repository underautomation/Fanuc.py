import typing
from UnderAutomation.Fanuc.Snpx.Internal import Assignment as assignment

class Assignment:
	'''Represents an SNPX memory assignment mapping a named element to a memory offset.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = assignment()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def offset(self) -> int:
		'''Gets the memory offset for this assignment. Negative if cleared.'''
		return self._instance.Offset

	@property
	def is_assignment_cleared(self) -> bool:
		'''Gets a value indicating whether this assignment has been cleared.'''
		return self._instance.IsAssignmentCleared

	@property
	def name(self) -> str:
		'''Gets the display name of this assignment.'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Assignment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
