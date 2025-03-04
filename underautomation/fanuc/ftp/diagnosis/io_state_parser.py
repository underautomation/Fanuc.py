import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.io_state import IOState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import IOStateParser as io_state_parser

class IOStateParser(SectionParser1[IOState]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_state_parser()
		else:
			self._instance = _internal
	def parse_line(self, line: str) -> None:
		self._instance.ParseLine(line)
	def after_parse(self) -> None:
		self._instance.AfterParse()
	@property
	def section_start(self) -> str:
		return self._instance.SectionStart
