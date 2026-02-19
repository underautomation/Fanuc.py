import typing
from underautomation.fanuc.ftp.internal.section_parser_1 import SectionParser1
from underautomation.fanuc.ftp.diagnosis.features import Features
from UnderAutomation.Fanuc.Ftp.Diagnosis import FeaturesParser as features_parser

class FeaturesParser(SectionParser1[Features]):
	'''Parser for reading and interpreting controller feature data from diagnostic files.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = features_parser()
		else:
			self._instance = _internal

	def parse_line(self, line: str) -> None:
		self._instance.ParseLine(line)

	def after_parse(self) -> None:
		self._instance.AfterParse()

	@property
	def section_start(self) -> typing.List[str]:
		return self._instance.SectionStart

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FeaturesParser):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
