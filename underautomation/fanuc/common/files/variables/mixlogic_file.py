from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.dryrun_variable_type import DryrunVariableType
from underautomation.fanuc.common.files.variables.dryrun_port_variable_type import DryrunPortVariableType
from underautomation.fanuc.common.files.variables.mix_bg_variable_type import MixBgVariableType
from underautomation.fanuc.common.files.variables.mix_logic_variable_type import MixLogicVariableType
from underautomation.fanuc.common.files.variables.mix_mkr_variable_type import MixMkrVariableType
from underautomation.fanuc.common.files.variables.on_path_variable_type import OnPathVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import MixlogicFile as mixlogic_file

class MixlogicFile(GenericVariableFile):
	'''Describes the Fanuc variable file mixlogic.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mixlogic_file()
		else:
			self._instance = _internal

	@property
	def dryrun(self) -> DryrunVariableType:
		'''Value of variable $DRYRUN'''
		__r = self._instance.Dryrun
		return None if __r is None else DryrunVariableType(__r)

	@property
	def dryrun_port(self) -> typing.List[DryrunPortVariableType]:
		'''Value of variable $DRYRUN_PORT'''
		__r = self._instance.DryrunPort
		return None if __r is None else [None if x is None else DryrunPortVariableType(x) for x in __r]

	@property
	def dryrun_sub(self) -> typing.List[str]:
		'''Value of variable $DRYRUN_SUB'''
		return self._instance.DryrunSub

	@property
	def mix_bg(self) -> typing.List[MixBgVariableType]:
		'''Value of variable $MIX_BG'''
		__r = self._instance.MixBg
		return None if __r is None else [None if x is None else MixBgVariableType(x) for x in __r]

	@property
	def mix_logic(self) -> MixLogicVariableType:
		'''Value of variable $MIX_LOGIC'''
		__r = self._instance.MixLogic
		return None if __r is None else MixLogicVariableType(__r)

	@property
	def mix_mkr(self) -> typing.List[MixMkrVariableType]:
		'''Value of variable $MIX_MKR'''
		__r = self._instance.MixMkr
		return None if __r is None else [None if x is None else MixMkrVariableType(x) for x in __r]

	@property
	def on_path(self) -> OnPathVariableType:
		'''Value of variable $ON_PATH'''
		__r = self._instance.OnPath
		return None if __r is None else OnPathVariableType(__r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MixlogicFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
