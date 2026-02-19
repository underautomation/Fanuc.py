import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import PalregFile as palreg_file

class PalregFile(GenericVariableFile):
	'''Describes the Fanuc variable file palreg.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = palreg_file()
		else:
			self._instance = _internal

	@property
	def palregnum(self) -> int:
		'''Value of variable $PALREGNUM'''
		return self._instance.Palregnum

	@property
	def palreg(self) -> typing.List[int]:
		'''Value of variable $PALREG'''
		return self._instance.Palreg

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PalregFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
