import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlmrGrpVariableType as plmr_grp_variable_type

class PlmrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PLMR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plmr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def pyld_enb(self) -> bool:
		'''Value of variable $PYLD_ENB'''
		return self._instance.PyldEnb

	@property
	def wmr_enb(self) -> bool:
		'''Value of variable $WMR_ENB'''
		return self._instance.WmrEnb

	@property
	def angle(self) -> float:
		'''Value of variable $ANGLE'''
		return self._instance.Angle

	@property
	def plmr_aa(self) -> float:
		'''Value of variable $PLMR_AA'''
		return self._instance.PlmrAa

	@property
	def plmr_bb(self) -> float:
		'''Value of variable $PLMR_BB'''
		return self._instance.PlmrBb

	@property
	def plmr_cc(self) -> float:
		'''Value of variable $PLMR_CC'''
		return self._instance.PlmrCc

	@property
	def plmr_dd(self) -> float:
		'''Value of variable $PLMR_DD'''
		return self._instance.PlmrDd

	@property
	def plst_ang(self) -> typing.List[float]:
		'''Value of variable $PLST_ANG'''
		return self._instance.PlstAng

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def max_xy_loc(self) -> float:
		'''Value of variable $MAX_XY_LOC'''
		return self._instance.MaxXyLoc

	@property
	def max_z_loc(self) -> float:
		'''Value of variable $MAX_Z_LOC'''
		return self._instance.MaxZLoc

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlmrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
