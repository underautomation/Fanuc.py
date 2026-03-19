import typing
from UnderAutomation.Fanuc.Snpx.Internal import StringRegisterSpan as string_register_span

class StringRegisterSpan:
	'''Defines a span within a string register, specifying the register index, start position, and length.'''
	def __init__(self, registerIndex: int, stringLength: int, stringStartIndex: int, _internal = 0):
		'''Creates a new instance with the specified register index, string length, and optional start index.

		:param registerIndex: The register index (1-based).
		:param stringLength: The number of characters (must be even, >= 2).
		:param stringStartIndex: The start index within the string (must be even, >= 0).
		'''
		if(_internal == 0):
			self._instance = string_register_span(registerIndex, stringLength, stringStartIndex)
		else:
			self._instance = _internal

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	@property
	def register_index(self) -> int:
		'''Register index, starts from 1'''
		return self._instance.RegisterIndex

	@register_index.setter
	def register_index(self, value: int):
		self._instance.RegisterIndex = value

	@property
	def string_start_index(self) -> int:
		'''String start index of the string to manipulate. Default : 0 (beginning of the string). Must be even and non-negative.'''
		return self._instance.StringStartIndex

	@string_start_index.setter
	def string_start_index(self, value: int):
		self._instance.StringStartIndex = value

	@property
	def string_length(self) -> int:
		'''Number of characters to return, should be an even number. Default : 80. Must be even, >= 2.'''
		return self._instance.StringLength

	@string_length.setter
	def string_length(self, value: int):
		self._instance.StringLength = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringRegisterSpan):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
