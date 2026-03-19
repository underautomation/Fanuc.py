import typing
from underautomation.fanuc.snpx.internal.comment_type import CommentType
from UnderAutomation.Fanuc.Snpx.Internal import CommentData as comment_data
from UnderAutomation.Fanuc.Snpx.Internal import CommentType as comment_type

class CommentData:
	'''Specifies the data type, index, and string length for reading or writing a comment via SNPX.'''
	def __init__(self, type: CommentType, index: int, stringLength: int, _internal = 0):
		'''Creates a new instance with the specified type, index, and optional string length.

		:param type: The type of data to read the comment for.
		:param index: The 1-based index of the element.
		:param stringLength: The number of characters (must be even, >= 2). Default is 16.
		'''
		if(_internal == 0):
			self._instance = comment_data(type, index, stringLength)
		else:
			self._instance = _internal

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	@property
	def type(self) -> CommentType:
		'''The type of data to read the comment for.'''
		return CommentType(int(self._instance.Type))

	@type.setter
	def type(self, value: CommentType):
		self._instance.Type = comment_type(int(value))

	@property
	def index(self) -> int:
		'''The 1-based index of the element. Must be >= 1.'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def string_length(self) -> int:
		'''Number of characters to read/write. Must be even, >= 2. Default is 16.'''
		return self._instance.StringLength

	@string_length.setter
	def string_length(self, value: int):
		self._instance.StringLength = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CommentData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
