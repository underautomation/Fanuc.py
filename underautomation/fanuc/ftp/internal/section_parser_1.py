import typing
from underautomation.fanuc.ftp.internal.section_parser import SectionParser
from UnderAutomation.Fanuc.Ftp.Internal import SectionParser as section_parser_1

T = typing.TypeVar('T')
class SectionParser1(SectionParser, typing.Generic[T]):
	'''Abstract generic section parser that creates and populates a section of type T.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SectionParser`1 class.'''
		if(_internal == 0):
			self._instance = section_parser_1()
		else:
			self._instance = _internal

	@property
	def section(self) -> T:
		'''The parsed section instance.'''
		return self._instance.Section

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SectionParser1):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
