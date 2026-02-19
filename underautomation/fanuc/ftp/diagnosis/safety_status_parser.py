import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
from UnderAutomation.Fanuc.Ftp.Diagnosis import SafetyStatusParser as safety_status_parser

class SafetyStatusParser(SectionParser1[SafetyStatus]):
	'''Parser for reading and interpreting safety status signals from diagnostic files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_status_parser()
		else:
			self._instance = _internal

	def parse_line(self, line: str, start: str, setValue: typing.Any) -> None:
		self._instance.ParseLine(line, start, setValue)

	@property
	def section_start(self) -> typing.List[str]:
		return self._instance.SectionStart

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyStatusParser):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
