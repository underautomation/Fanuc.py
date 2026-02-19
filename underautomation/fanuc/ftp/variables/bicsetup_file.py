import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import BicsetupFile as bicsetup_file

class BicsetupFile(GenericVariableFile):
	'''Describes the Fanuc variable file bicsetup.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bicsetup_file()
		else:
			self._instance = _internal

	@property
	def bic_name(self) -> str:
		'''Value of variable BIC_NAME'''
		return self._instance.BicName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BicsetupFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
