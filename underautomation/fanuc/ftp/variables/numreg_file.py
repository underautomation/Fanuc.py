import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import NumregFile as numreg_file

class NumregFile(GenericVariableFile):
	'''Describes the Fanuc variable file numreg.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numreg_file()
		else:
			self._instance = _internal

	@property
	def numreg(self) -> typing.List[float]:
		'''Value of variable $NUMREG'''
		return self._instance.Numreg

	@property
	def maxregnum(self) -> int:
		'''Value of variable $MAXREGNUM'''
		return self._instance.Maxregnum

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumregFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
