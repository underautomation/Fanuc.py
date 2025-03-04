import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import SectionParser as section_parser

class SectionParser:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = section_parser()
		else:
			self._instance = _internal
	def can_handle_section(self, line: str) -> bool:
		return self._instance.CanHandleSection(line)
	def parse_line(self, line: str) -> None:
		self._instance.ParseLine(line)
	def after_parse(self) -> None:
		self._instance.AfterParse()
	@property
	def section_start(self) -> str:
		return self._instance.SectionStart
	@property
	def end_of_file(self) -> bool:
		return self._instance.EndOfFile
	@end_of_file.setter
	def end_of_file(self, value: bool):
		self._instance.EndOfFile = value
