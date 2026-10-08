from __future__ import annotations
import typing
from underautomation.fanuc.common.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.common.vector_variable import VectorVariable
from underautomation.fanuc.common.files.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Common.Files.Variables import CellGrpVariableType as cell_grp_variable_type

class CellGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type CELL_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cell_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def cell_frame(self) -> CartesianPositionVariable:
		'''Value of variable $CELL_FRAME'''
		__r = self._instance.CellFrame
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@property
	def mount_loc(self) -> CartesianPositionVariable:
		'''Value of variable $MOUNT_LOC'''
		__r = self._instance.MountLoc
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@property
	def cf_method(self) -> int:
		'''Value of variable $CF_METHOD'''
		return self._instance.CfMethod

	@property
	def cpy_src_idx(self) -> int:
		'''Value of variable $CPY_SRC_IDX'''
		return self._instance.CpySrcIdx

	@property
	def platfrm_ofs(self) -> CartesianPositionVariable:
		'''Value of variable $PLATFRM_OFS'''
		__r = self._instance.PlatfrmOfs
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@property
	def platfrm_dim(self) -> VectorVariable:
		'''Value of variable $PLATFRM_DIM'''
		__r = self._instance.PlatfrmDim
		return None if __r is None else VectorVariable(__r)

	@property
	def base_offset(self) -> CartesianPositionVariable:
		'''Value of variable $BASE_OFFSET'''
		__r = self._instance.BaseOffset
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@property
	def base_dim(self) -> VectorVariable:
		'''Value of variable $BASE_DIM'''
		__r = self._instance.BaseDim
		return None if __r is None else VectorVariable(__r)

	@property
	def aux_order(self) -> typing.List[int]:
		'''Value of variable $AUX_ORDER'''
		return self._instance.AuxOrder

	@property
	def aux_xyz_map(self) -> typing.List[int]:
		'''Value of variable $AUX_XYZ_MAP'''
		return self._instance.AuxXyzMap

	@property
	def aux_offset(self) -> typing.List[float]:
		'''Value of variable $AUX_OFFSET'''
		return self._instance.AuxOffset

	@property
	def aux_length(self) -> typing.List[float]:
		'''Value of variable $AUX_LENGTH'''
		return self._instance.AuxLength

	@property
	def attch_gp_ms(self) -> int:
		'''Value of variable $ATTCH_GP_MS'''
		return self._instance.AttchGpMs

	@property
	def autorail(self) -> int:
		'''Value of variable $AUTORAIL'''
		return self._instance.Autorail

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CellGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
