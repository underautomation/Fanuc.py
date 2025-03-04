import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.program_states import ProgramStates
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import ProgramStatesParser as program_states_parser

class ProgramStatesParser(SectionParser1[ProgramStates]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_states_parser()
		else:
			self._instance = _internal
	def parse_line(self, line: str) -> None:
		self._instance.ParseLine(line)
	def after_parse(self) -> None:
		self._instance.AfterParse()
	@property
	def section_start(self) -> str:
		return self._instance.SectionStart
