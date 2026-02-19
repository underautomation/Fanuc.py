import typing
from UnderAutomation.Fanuc.Ftp.Internal import SectionParser as section_parser

class SectionParser:
	'''Abstract base class for parsing sections of diagnostic files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = section_parser()
		else:
			self._instance = _internal

	def can_handle_section(self, line: str) -> bool:
		'''Determines whether this parser can handle the given section header line.

		:param line: The header line to check.
		:returns: true if this parser handles the section; otherwise false.
		'''
		return self._instance.CanHandleSection(line)

	def parse_line(self, line: str) -> None:
		'''Parses a single line from the section content.

		:param line: The line to parse.
		'''
		self._instance.ParseLine(line)

	def after_parse(self) -> None:
		'''Called after all lines have been parsed. Override to perform final processing.'''
		self._instance.AfterParse()

	@property
	def section_start(self) -> typing.List[str]:
		'''Gets the possible section header strings that indicate the start of this section.'''
		return self._instance.SectionStart

	@property
	def end_of_file(self) -> bool:
		'''Gets or sets a value indicating whether the end of the file or section has been reached.'''
		return self._instance.EndOfFile

	@end_of_file.setter
	def end_of_file(self, value: bool):
		self._instance.EndOfFile = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SectionParser):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
