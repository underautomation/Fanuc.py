import typing
from underautomation.fanuc.ftp.variables.sbr_variable_type import SbrVariableType
from underautomation.fanuc.ftp.variables.sbr2_variable_type import Sbr2VariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SysservoFile as sysservo_file

class SysservoFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysservo.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysservo_file()
		else:
			self._instance = _internal

	@property
	def sbr(self) -> typing.List[SbrVariableType]:
		'''Value of variable $SBR'''
		return [SbrVariableType(x) for x in self._instance.Sbr]

	@property
	def sbr2(self) -> typing.List[Sbr2VariableType]:
		'''Value of variable $SBR2'''
		return [Sbr2VariableType(x) for x in self._instance.Sbr2]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysservoFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
