import typing
from underautomation.fanuc.ftp.variables.dryrun_variable_type import DryrunVariableType
from underautomation.fanuc.ftp.variables.dryrun_port_variable_type import DryrunPortVariableType
from underautomation.fanuc.ftp.variables.mix_bg_variable_type import MixBgVariableType
from underautomation.fanuc.ftp.variables.mix_logic_variable_type import MixLogicVariableType
from underautomation.fanuc.ftp.variables.mix_mkr_variable_type import MixMkrVariableType
from underautomation.fanuc.ftp.variables.on_path_variable_type import OnPathVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MixlogicFile as mixlogic_file

class MixlogicFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mixlogic_file()
		else:
			self._instance = _internal
	@property
	def dryrun(self) -> DryrunVariableType:
		return DryrunVariableType(self._instance.Dryrun)
	@property
	def dryrun_port(self) -> typing.List[DryrunPortVariableType]:
		return [DryrunPortVariableType(x) for x in self._instance.DryrunPort]
	@property
	def dryrun_sub(self) -> typing.List[str]:
		return self._instance.DryrunSub
	@property
	def mix_bg(self) -> typing.List[MixBgVariableType]:
		return [MixBgVariableType(x) for x in self._instance.MixBg]
	@property
	def mix_logic(self) -> MixLogicVariableType:
		return MixLogicVariableType(self._instance.MixLogic)
	@property
	def mix_mkr(self) -> typing.List[MixMkrVariableType]:
		return [MixMkrVariableType(x) for x in self._instance.MixMkr]
	@property
	def on_path(self) -> OnPathVariableType:
		return OnPathVariableType(self._instance.OnPath)
