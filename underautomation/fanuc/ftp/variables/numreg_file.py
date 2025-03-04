import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import NumregFile as numreg_file

class NumregFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numreg_file()
		else:
			self._instance = _internal
	@property
	def numreg(self) -> typing.List[float]:
		return self._instance.Numreg
	@property
	def maxregnum(self) -> int:
		return self._instance.Maxregnum
