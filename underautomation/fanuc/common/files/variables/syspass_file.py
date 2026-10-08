from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.passname_variable_type import PassnameVariableType
from underautomation.fanuc.common.files.variables.password_variable_type import PasswordVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SyspassFile as syspass_file

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
		__r = self._instance.Passname
		return None if __r is None else [None if x is None else PassnameVariableType(x) for x in __r]

	@property
	def passsuper(self) -> PassnameVariableType:
		'''Value of variable $PASSSUPER'''
		__r = self._instance.Passsuper
		return None if __r is None else PassnameVariableType(__r)

	@property
	def password(self) -> PasswordVariableType:
		'''Value of variable $PASSWORD'''
		__r = self._instance.Password
		return None if __r is None else PasswordVariableType(__r)

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
