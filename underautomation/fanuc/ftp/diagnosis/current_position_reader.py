import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
from UnderAutomation.Fanuc.Ftp.Diagnosis import CurrentPositionReader as current_position_reader

class CurrentPositionReader(SectionParser1[CurrentPosition]):
	'''Parser for reading and interpreting current robot position data from diagnostic files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position_reader()
		else:
			self._instance = _internal

	def after_parse(self) -> None:
		self._instance.AfterParse()

	def parse_line(self, line: str) -> None:
		self._instance.ParseLine(line)

	@property
	def section_start(self) -> typing.List[str]:
		return self._instance.SectionStart

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentPositionReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
