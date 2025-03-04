import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.vector_variable import VectorVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CellGrpVariableType as cell_grp_variable_type

class CellGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cell_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def cell_frame(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CellFrame)
	@property
	def mount_loc(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.MountLoc)
	@property
	def cf_method(self) -> int:
		return self._instance.CfMethod
	@property
	def cpy_src_idx(self) -> int:
		return self._instance.CpySrcIdx
	@property
	def platfrm_ofs(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.PlatfrmOfs)
	@property
	def platfrm_dim(self) -> VectorVariable:
		return VectorVariable(self._instance.PlatfrmDim)
	@property
	def base_offset(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.BaseOffset)
	@property
	def base_dim(self) -> VectorVariable:
		return VectorVariable(self._instance.BaseDim)
	@property
	def aux_order(self) -> typing.List[int]:
		return self._instance.AuxOrder
	@property
	def aux_xyz_map(self) -> typing.List[int]:
		return self._instance.AuxXyzMap
	@property
	def aux_offset(self) -> typing.List[float]:
		return self._instance.AuxOffset
	@property
	def aux_length(self) -> typing.List[float]:
		return self._instance.AuxLength
	@property
	def attch_gp_ms(self) -> int:
		return self._instance.AttchGpMs
	@property
	def autorail(self) -> int:
		return self._instance.Autorail
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
