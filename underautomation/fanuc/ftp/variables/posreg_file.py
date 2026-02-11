import typing
from underautomation.fanuc.ftp.variables.position_register import PositionRegister
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PosregFile as posreg_file

class PosregFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = posreg_file()
		else:
			self._instance = _internal
	@property
	def posreg(self) -> typing.List[PositionRegister]:
		return [PositionRegister(None, None, x) for x in self._instance.Posreg]
	@property
	def maxpregnum(self) -> int:
		return self._instance.Maxpregnum
