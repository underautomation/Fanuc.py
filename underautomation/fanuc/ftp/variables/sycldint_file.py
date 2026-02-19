import typing
from underautomation.fanuc.ftp.variables.jcr_variable_type import JcrVariableType
from underautomation.fanuc.ftp.variables.jcr_grp_variable_type import JcrGrpVariableType
from underautomation.fanuc.ftp.variables.mcr_variable_type import McrVariableType
from underautomation.fanuc.ftp.variables.mcr_grp_variable_type import McrGrpVariableType
from underautomation.fanuc.ftp.variables.mor_variable_type import MorVariableType
from underautomation.fanuc.ftp.variables.mor_grp_variable_type import MorGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SycldintFile as sycldint_file

class SycldintFile(GenericVariableFile):
	'''Describes the Fanuc variable file sycldint.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sycldint_file()
		else:
			self._instance = _internal

	@property
	def erseverity(self) -> int:
		'''Value of variable $ERSEVERITY'''
		return self._instance.Erseverity

	@property
	def jcr(self) -> JcrVariableType:
		'''Value of variable $JCR'''
		return JcrVariableType(self._instance.Jcr)

	@property
	def jcr_grp(self) -> typing.List[JcrGrpVariableType]:
		'''Value of variable $JCR_GRP'''
		return [JcrGrpVariableType(x) for x in self._instance.JcrGrp]

	@property
	def load_device(self) -> str:
		'''Value of variable $LOAD_DEVICE'''
		return self._instance.LoadDevice

	@property
	def mcr(self) -> McrVariableType:
		'''Value of variable $MCR'''
		return McrVariableType(self._instance.Mcr)

	@property
	def mcr_grp(self) -> typing.List[McrGrpVariableType]:
		'''Value of variable $MCR_GRP'''
		return [McrGrpVariableType(x) for x in self._instance.McrGrp]

	@property
	def mor(self) -> MorVariableType:
		'''Value of variable $MOR'''
		return MorVariableType(self._instance.Mor)

	@property
	def mor_grp(self) -> typing.List[MorGrpVariableType]:
		'''Value of variable $MOR_GRP'''
		return [MorGrpVariableType(x) for x in self._instance.MorGrp]

	@property
	def pwr_up_rtn(self) -> typing.List[str]:
		'''Value of variable $PWR_UP_RTN'''
		return self._instance.PwrUpRtn

	@property
	def tpabrt_used(self) -> bool:
		'''Value of variable $TPABRT_USED'''
		return self._instance.TpabrtUsed

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SycldintFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
