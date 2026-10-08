from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.sbr_variable_type import SbrVariableType
from underautomation.fanuc.common.files.variables.sbr2_variable_type import Sbr2VariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SysservoFile as sysservo_file

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
		__r = self._instance.Sbr
		return None if __r is None else [None if x is None else SbrVariableType(x) for x in __r]

	@property
	def sbr2(self) -> typing.List[Sbr2VariableType]:
		'''Value of variable $SBR2'''
		__r = self._instance.Sbr2
		return None if __r is None else [None if x is None else Sbr2VariableType(x) for x in __r]

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
