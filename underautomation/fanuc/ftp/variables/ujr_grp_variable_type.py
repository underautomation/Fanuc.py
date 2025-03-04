import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UjrGrpVariableType as ujr_grp_variable_type

class UjrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ujr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def fine_ovrd(self) -> int:
		return self._instance.FineOvrd
	@property
	def jogframe(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Jogframe)
	@property
	def fine_dist(self) -> float:
		return self._instance.FineDist
	@property
	def j7_group(self) -> int:
		return self._instance.J7Group
	@property
	def j8_group(self) -> int:
		return self._instance.J8Group
	@property
	def j7_axis(self) -> int:
		return self._instance.J7Axis
	@property
	def j8_axis(self) -> int:
		return self._instance.J8Axis
	@property
	def j7_label(self) -> str:
		return self._instance.J7Label
	@property
	def j8_label(self) -> str:
		return self._instance.J8Label
	@property
	def j7_graphic(self) -> str:
		return self._instance.J7Graphic
	@property
	def j8_graphic(self) -> str:
		return self._instance.J8Graphic
	@property
	def dsb_j7j8(self) -> bool:
		return self._instance.DsbJ7j8
	@property
	def dsbl_key(self) -> typing.List[bool]:
		return self._instance.DsblKey
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
