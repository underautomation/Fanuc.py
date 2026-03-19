import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
from underautomation.fanuc.snpx.internal.comment_data import CommentData
from UnderAutomation.Fanuc.Snpx.Assignment import CommentBatchAssignment as comment_batch_assignment

class CommentBatchAssignment(BatchAssignment2[str, CommentData]):
	'''Batch assignment for reading multiple comments at once.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CommentBatchAssignment class.'''
		if(_internal == 0):
			self._instance = comment_batch_assignment()
		else:
			self._instance = _internal

	def read(self) -> typing.List[str]:
		'''Reads all comments assigned in this batch.

		:returns: An array of comment strings.
		'''
		return self._instance.Read()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommentBatchAssignment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
