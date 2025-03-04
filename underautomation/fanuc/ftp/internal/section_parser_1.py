import typing
from underautomation.fanuc.ftp.internal.section_parser import SectionParser
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import SectionParser as section_parser_1

T = typing.TypeVar('T')
class SectionParser1(SectionParser, typing.Generic[T]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = section_parser_1()
		else:
			self._instance = _internal
	@property
	def section(self) -> T:
		return self._instance.Section
