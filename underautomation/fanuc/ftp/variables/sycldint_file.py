import typing
from underautomation.fanuc.ftp.variables.jcr_variable_type import JcrVariableType
from underautomation.fanuc.ftp.variables.jcr_grp_variable_type import JcrGrpVariableType
from underautomation.fanuc.ftp.variables.mcr_variable_type import McrVariableType
from underautomation.fanuc.ftp.variables.mcr_grp_variable_type import McrGrpVariableType
from underautomation.fanuc.ftp.variables.mor_variable_type import MorVariableType
from underautomation.fanuc.ftp.variables.mor_grp_variable_type import MorGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SycldintFile as sycldint_file

class SycldintFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sycldint_file()
		else:
			self._instance = _internal
	@property
	def erseverity(self) -> int:
		return self._instance.Erseverity
	@property
	def jcr(self) -> JcrVariableType:
		return JcrVariableType(self._instance.Jcr)
	@property
	def jcr_grp(self) -> typing.List[JcrGrpVariableType]:
		return [JcrGrpVariableType(x) for x in self._instance.JcrGrp]
	@property
	def load_device(self) -> str:
		return self._instance.LoadDevice
	@property
	def mcr(self) -> McrVariableType:
		return McrVariableType(self._instance.Mcr)
	@property
	def mcr_grp(self) -> typing.List[McrGrpVariableType]:
		return [McrGrpVariableType(x) for x in self._instance.McrGrp]
	@property
	def mor(self) -> MorVariableType:
		return MorVariableType(self._instance.Mor)
	@property
	def mor_grp(self) -> typing.List[MorGrpVariableType]:
		return [MorGrpVariableType(x) for x in self._instance.MorGrp]
	@property
	def pwr_up_rtn(self) -> typing.List[str]:
		return self._instance.PwrUpRtn
	@property
	def tpabrt_used(self) -> bool:
		return self._instance.TpabrtUsed
