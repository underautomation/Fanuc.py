import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.cell_grp_variable_type import CellGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysframeFile as sysframe_file

class SysframeFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysframe_file()
		else:
			self._instance = _internal
	@property
	def cell_floor(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CellFloor)
	@property
	def cell_grp(self) -> typing.List[CellGrpVariableType]:
		return [CellGrpVariableType(x) for x in self._instance.CellGrp]
	@property
	def mnuframe(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.Mnuframe]
	@property
	def mnuframenum(self) -> typing.List[int]:
		return self._instance.Mnuframenum
	@property
	def mnutool(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.Mnutool]
	@property
	def mnutoolnum(self) -> typing.List[int]:
		return self._instance.Mnutoolnum
