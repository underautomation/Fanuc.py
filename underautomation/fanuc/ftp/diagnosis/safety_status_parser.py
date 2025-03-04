import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.safety_status import SafetyStatus
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import SafetyStatusParser as safety_status_parser

class SafetyStatusParser(SectionParser1[SafetyStatus]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = safety_status_parser()
		else:
			self._instance = _internal
	def parse_line(self, line: str, start: str, setValue: typing.Any) -> None:
		self._instance.ParseLine(line, start, setValue)
	@property
	def section_start(self) -> str:
		return self._instance.SectionStart
