import typing
from underautomation.fanuc.ftp.variables.cellset_variable_type import CellsetVariableType
from underautomation.fanuc.ftp.variables.clmlio_variable_type import ClmlioVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CellioFile as cellio_file

class CellioFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cellio_file()
		else:
			self._instance = _internal
	@property
	def cell_option(self) -> bool:
		return self._instance.CellOption
	@property
	def cell_setup(self) -> CellsetVariableType:
		return CellsetVariableType(self._instance.CellSetup)
	@property
	def clmlio(self) -> typing.List[ClmlioVariableType]:
		return [ClmlioVariableType(x) for x in self._instance.Clmlio]
	@property
	def style_comnt(self) -> typing.List[str]:
		return self._instance.StyleComnt
	@property
	def style_count(self) -> int:
		return self._instance.StyleCount
	@property
	def style_enab(self) -> typing.List[bool]:
		return self._instance.StyleEnab
	@property
	def style_menu(self) -> int:
		return self._instance.StyleMenu
	@property
	def style_name(self) -> typing.List[str]:
		return self._instance.StyleName
