import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import StrregFile as strreg_file

class StrregFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = strreg_file()
		else:
			self._instance = _internal
	@property
	def strreg(self) -> typing.List[str]:
		return self._instance.Strreg
	@property
	def maxsregnum(self) -> int:
		return self._instance.Maxsregnum
