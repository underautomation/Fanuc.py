import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.current_position import CurrentPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import CurrentPositionReader as current_position_reader

class CurrentPositionReader(SectionParser1[CurrentPosition]):
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
	def section_start(self) -> str:
		return self._instance.SectionStart
