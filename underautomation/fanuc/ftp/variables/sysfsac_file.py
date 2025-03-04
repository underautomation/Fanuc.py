import typing
from underautomation.fanuc.ftp.variables.fsac_lst_variable_type import FsacLstVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysfsacFile as sysfsac_file

class SysfsacFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysfsac_file()
		else:
			self._instance = _internal
	@property
	def fsac_def_lv(self) -> int:
		return self._instance.FsacDefLv
	@property
	def fsac_enable(self) -> int:
		return self._instance.FsacEnable
	@property
	def fsac_list(self) -> typing.List[FsacLstVariableType]:
		return [FsacLstVariableType(x) for x in self._instance.FsacList]
