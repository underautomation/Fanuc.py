import typing
from underautomation.fanuc.ftp.variables.fsac_lst_variable_type import FsacLstVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SysfsacFile as sysfsac_file

class SysfsacFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysfsac.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysfsac_file()
		else:
			self._instance = _internal

	@property
	def fsac_def_lv(self) -> int:
		'''Value of variable $FSAC_DEF_LV'''
		return self._instance.FsacDefLv

	@property
	def fsac_enable(self) -> int:
		'''Value of variable $FSAC_ENABLE'''
		return self._instance.FsacEnable

	@property
	def fsac_list(self) -> typing.List[FsacLstVariableType]:
		'''Value of variable $FSAC_LIST'''
		return [FsacLstVariableType(x) for x in self._instance.FsacList]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysfsacFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
