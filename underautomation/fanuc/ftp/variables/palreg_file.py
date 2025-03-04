import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PalregFile as palreg_file

class PalregFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = palreg_file()
		else:
			self._instance = _internal
	@property
	def palregnum(self) -> int:
		return self._instance.Palregnum
	@property
	def palreg(self) -> typing.List[int]:
		return self._instance.Palreg
