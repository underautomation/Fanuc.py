import typing
from underautomation.fanuc.snpx.internal.comment_type import CommentType
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.internal.comment_data import CommentData
from underautomation.fanuc.snpx.assignment.comment_batch_assignment import CommentBatchAssignment
from UnderAutomation.Fanuc.Snpx.Internal import Comments as comments
from UnderAutomation.Fanuc.Snpx.Internal import CommentType as comment_type

class Comments(SnpxWritableAssignableElements3[str, CommentData, CommentBatchAssignment]):
	'''Provides read/write access to comments of registers, I/O signals and other data via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = comments()
		else:
			self._instance = _internal

	def read(self, type: CommentType, index: int, stringLength: int=16) -> str:
		'''Reads the comment for the specified data type and index.

		:param type: The type of data.
		:param index: The 1-based element index.
		:param stringLength: The number of characters to read (must be even, >= 2). Default is 16.
		:returns: The comment string.
		'''
		return self._instance.Read(comment_type(int(type)), index, stringLength)

	def write(self, type: CommentType, index: int, value: str, stringLength: int=16) -> None:
		'''Writes a comment for the specified data type and index.

		:param type: The type of data.
		:param index: The 1-based element index.
		:param value: The comment string to write.
		:param stringLength: The number of characters to write (must be even, >= 2). Default is 16.
		'''
		self._instance.Write(comment_type(int(type)), index, value, stringLength)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Comments):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
