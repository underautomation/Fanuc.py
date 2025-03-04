import typing
from underautomation.fanuc.ftp.variables.passname_variable_type import PassnameVariableType
from underautomation.fanuc.ftp.variables.password_variable_type import PasswordVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SyspassFile as syspass_file

class SyspassFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syspass_file()
		else:
			self._instance = _internal
	@property
	def passname(self) -> typing.List[PassnameVariableType]:
		return [PassnameVariableType(x) for x in self._instance.Passname]
	@property
	def passsuper(self) -> PassnameVariableType:
		return PassnameVariableType(self._instance.Passsuper)
	@property
	def password(self) -> PasswordVariableType:
		return PasswordVariableType(self._instance.Password)
