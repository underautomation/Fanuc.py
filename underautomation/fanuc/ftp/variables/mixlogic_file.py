import typing
from underautomation.fanuc.ftp.variables.dryrun_variable_type import DryrunVariableType
from underautomation.fanuc.ftp.variables.dryrun_port_variable_type import DryrunPortVariableType
from underautomation.fanuc.ftp.variables.mix_bg_variable_type import MixBgVariableType
from underautomation.fanuc.ftp.variables.mix_logic_variable_type import MixLogicVariableType
from underautomation.fanuc.ftp.variables.mix_mkr_variable_type import MixMkrVariableType
from underautomation.fanuc.ftp.variables.on_path_variable_type import OnPathVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import MixlogicFile as mixlogic_file

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
		return DryrunVariableType(self._instance.Dryrun)

	@property
	def dryrun_port(self) -> typing.List[DryrunPortVariableType]:
		'''Value of variable $DRYRUN_PORT'''
		return [DryrunPortVariableType(x) for x in self._instance.DryrunPort]

	@property
	def dryrun_sub(self) -> typing.List[str]:
		'''Value of variable $DRYRUN_SUB'''
		return self._instance.DryrunSub

	@property
	def mix_bg(self) -> typing.List[MixBgVariableType]:
		'''Value of variable $MIX_BG'''
		return [MixBgVariableType(x) for x in self._instance.MixBg]

	@property
	def mix_logic(self) -> MixLogicVariableType:
		'''Value of variable $MIX_LOGIC'''
		return MixLogicVariableType(self._instance.MixLogic)

	@property
	def mix_mkr(self) -> typing.List[MixMkrVariableType]:
		'''Value of variable $MIX_MKR'''
		return [MixMkrVariableType(x) for x in self._instance.MixMkr]

	@property
	def on_path(self) -> OnPathVariableType:
		'''Value of variable $ON_PATH'''
		return OnPathVariableType(self._instance.OnPath)

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
