import typing
from underautomation.fanuc.ftp.variables.position_register import PositionRegister
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import PosregFile as posreg_file

class PosregFile(GenericVariableFile):
	'''Describes the Fanuc variable file posreg.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = posreg_file()
		else:
			self._instance = _internal

	@property
	def posreg(self) -> typing.List[PositionRegister]:
		'''Value of variable $POSREG'''
		return [PositionRegister(None, None, x) for x in self._instance.Posreg]

	@property
	def maxpregnum(self) -> int:
		'''Value of variable $MAXPREGNUM'''
		return self._instance.Maxpregnum

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PosregFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
