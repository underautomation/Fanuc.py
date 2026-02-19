import typing
from underautomation.fanuc.ftp.variables.cellset_variable_type import CellsetVariableType
from underautomation.fanuc.ftp.variables.clmlio_variable_type import ClmlioVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import CellioFile as cellio_file

class CellioFile(GenericVariableFile):
	'''Describes the Fanuc variable file cellio.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cellio_file()
		else:
			self._instance = _internal

	@property
	def cell_option(self) -> bool:
		'''Value of variable $CELL_OPTION'''
		return self._instance.CellOption

	@property
	def cell_setup(self) -> CellsetVariableType:
		'''Value of variable $CELL_SETUP'''
		return CellsetVariableType(self._instance.CellSetup)

	@property
	def clmlio(self) -> typing.List[ClmlioVariableType]:
		'''Value of variable $CLMLIO'''
		return [ClmlioVariableType(x) for x in self._instance.Clmlio]

	@property
	def style_comnt(self) -> typing.List[str]:
		'''Value of variable $STYLE_COMNT'''
		return self._instance.StyleComnt

	@property
	def style_count(self) -> int:
		'''Value of variable $STYLE_COUNT'''
		return self._instance.StyleCount

	@property
	def style_enab(self) -> typing.List[bool]:
		'''Value of variable $STYLE_ENAB'''
		return self._instance.StyleEnab

	@property
	def style_menu(self) -> int:
		'''Value of variable $STYLE_MENU'''
		return self._instance.StyleMenu

	@property
	def style_name(self) -> typing.List[str]:
		'''Value of variable $STYLE_NAME'''
		return self._instance.StyleName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CellioFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
