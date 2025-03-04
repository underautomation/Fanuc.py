import typing
from underautomation.fanuc.ftp.variables.mn_mcr_table_variable_type import MnMcrTableVariableType
from underautomation.fanuc.ftp.variables.mn_mcr_sop_variable_type import MnMcrSopVariableType
from underautomation.fanuc.ftp.variables.mn_mcr_uop_variable_type import MnMcrUopVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysmacroFile as sysmacro_file

class SysmacroFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysmacro_file()
		else:
			self._instance = _internal
	@property
	def macrolduimt(self) -> bool:
		return self._instance.Macrolduimt
	@property
	def macromaxdri(self) -> int:
		return self._instance.Macromaxdri
	@property
	def macrotable(self) -> typing.List[MnMcrTableVariableType]:
		return [MnMcrTableVariableType(x) for x in self._instance.Macrotable]
	@property
	def macro_maxnu(self) -> int:
		return self._instance.MacroMaxnu
	@property
	def macrsopenbl(self) -> MnMcrSopVariableType:
		return MnMcrSopVariableType(self._instance.Macrsopenbl)
	@property
	def macrspdimsk(self) -> int:
		return self._instance.Macrspdimsk
	@property
	def macrspsumsk(self) -> int:
		return self._instance.Macrspsumsk
	@property
	def macrtpdsbex(self) -> bool:
		return self._instance.Macrtpdsbex
	@property
	def macruopenbl(self) -> MnMcrUopVariableType:
		return MnMcrUopVariableType(self._instance.Macruopenbl)
