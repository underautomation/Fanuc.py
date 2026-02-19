import typing
from underautomation.fanuc.ftp.variables.passname_variable_type import PassnameVariableType
from underautomation.fanuc.ftp.variables.password_variable_type import PasswordVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SyspassFile as syspass_file

class SyspassFile(GenericVariableFile):
	'''Describes the Fanuc variable file syspass.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syspass_file()
		else:
			self._instance = _internal

	@property
	def passname(self) -> typing.List[PassnameVariableType]:
		'''Value of variable $PASSNAME'''
		return [PassnameVariableType(x) for x in self._instance.Passname]

	@property
	def passsuper(self) -> PassnameVariableType:
		'''Value of variable $PASSSUPER'''
		return PassnameVariableType(self._instance.Passsuper)

	@property
	def password(self) -> PasswordVariableType:
		'''Value of variable $PASSWORD'''
		return PasswordVariableType(self._instance.Password)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SyspassFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
