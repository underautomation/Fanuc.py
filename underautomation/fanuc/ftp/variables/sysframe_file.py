import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.cell_grp_variable_type import CellGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SysframeFile as sysframe_file

class SysframeFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysframe.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysframe_file()
		else:
			self._instance = _internal

	@property
	def cell_floor(self) -> CartesianPositionVariable:
		'''Value of variable $CELL_FLOOR'''
		return CartesianPositionVariable(self._instance.CellFloor)

	@property
	def cell_grp(self) -> typing.List[CellGrpVariableType]:
		'''Value of variable $CELL_GRP'''
		return [CellGrpVariableType(x) for x in self._instance.CellGrp]

	@property
	def mnuframe(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $MNUFRAME'''
		return [CartesianPositionVariable(x) for x in self._instance.Mnuframe]

	@property
	def mnuframenum(self) -> typing.List[int]:
		'''Value of variable $MNUFRAMENUM'''
		return self._instance.Mnuframenum

	@property
	def mnutool(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $MNUTOOL'''
		return [CartesianPositionVariable(x) for x in self._instance.Mnutool]

	@property
	def mnutoolnum(self) -> typing.List[int]:
		'''Value of variable $MNUTOOLNUM'''
		return self._instance.Mnutoolnum

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysframeFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
