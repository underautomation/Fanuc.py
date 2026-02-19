import typing
from underautomation.fanuc.ftp.variables.mn_mcr_table_variable_type import MnMcrTableVariableType
from underautomation.fanuc.ftp.variables.mn_mcr_sop_variable_type import MnMcrSopVariableType
from underautomation.fanuc.ftp.variables.mn_mcr_uop_variable_type import MnMcrUopVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SysmacroFile as sysmacro_file

class SysmacroFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysmacro.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysmacro_file()
		else:
			self._instance = _internal

	@property
	def macrolduimt(self) -> bool:
		'''Value of variable $MACROLDUIMT'''
		return self._instance.Macrolduimt

	@property
	def macromaxdri(self) -> int:
		'''Value of variable $MACROMAXDRI'''
		return self._instance.Macromaxdri

	@property
	def macrotable(self) -> typing.List[MnMcrTableVariableType]:
		'''Value of variable $MACROTABLE'''
		return [MnMcrTableVariableType(x) for x in self._instance.Macrotable]

	@property
	def macro_maxnu(self) -> int:
		'''Value of variable $MACRO_MAXNU'''
		return self._instance.MacroMaxnu

	@property
	def macrsopenbl(self) -> MnMcrSopVariableType:
		'''Value of variable $MACRSOPENBL'''
		return MnMcrSopVariableType(self._instance.Macrsopenbl)

	@property
	def macrspdimsk(self) -> int:
		'''Value of variable $MACRSPDIMSK'''
		return self._instance.Macrspdimsk

	@property
	def macrspsumsk(self) -> int:
		'''Value of variable $MACRSPSUMSK'''
		return self._instance.Macrspsumsk

	@property
	def macrtpdsbex(self) -> bool:
		'''Value of variable $MACRTPDSBEX'''
		return self._instance.Macrtpdsbex

	@property
	def macruopenbl(self) -> MnMcrUopVariableType:
		'''Value of variable $MACRUOPENBL'''
		return MnMcrUopVariableType(self._instance.Macruopenbl)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysmacroFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
