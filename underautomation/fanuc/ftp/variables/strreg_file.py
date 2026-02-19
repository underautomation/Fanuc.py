import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import StrregFile as strreg_file

class StrregFile(GenericVariableFile):
	'''Describes the Fanuc variable file strreg.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = strreg_file()
		else:
			self._instance = _internal

	@property
	def strreg(self) -> typing.List[str]:
		'''Value of variable $STRREG'''
		return self._instance.Strreg

	@property
	def maxsregnum(self) -> int:
		'''Value of variable $MAXSREGNUM'''
		return self._instance.Maxsregnum

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StrregFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
