import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import Fmr2GrpVariableType as fmr2_grp_variable_type

class Fmr2GrpVariableType(GenericVariableType):
	'''Describes the Fanuc type FMR2_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fmr2_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def vel_rot(self) -> float:
		'''Value of variable $VEL_ROT'''
		return self._instance.VelRot

	@property
	def vel_lin(self) -> float:
		'''Value of variable $VEL_LIN'''
		return self._instance.VelLin

	@property
	def vel_mod(self) -> typing.List[int]:
		'''Value of variable $VEL_MOD'''
		return self._instance.VelMod

	@property
	def k_life(self) -> typing.List[float]:
		'''Value of variable $K_LIFE'''
		return self._instance.KLife

	@property
	def ntr_life(self) -> typing.List[float]:
		'''Value of variable $NTR_LIFE'''
		return self._instance.NtrLife

	@property
	def eff_rate(self) -> typing.List[float]:
		'''Value of variable $EFF_RATE'''
		return self._instance.EffRate

	@property
	def rot_inrt(self) -> typing.List[float]:
		'''Value of variable $ROT_INRT'''
		return self._instance.RotInrt

	@property
	def trov_max(self) -> typing.List[float]:
		'''Value of variable $TROV_MAX'''
		return self._instance.TrovMax

	@property
	def t_life0(self) -> float:
		'''Value of variable $T_LIFE_0'''
		return self._instance.TLife0

	@property
	def rated_trq(self) -> typing.List[float]:
		'''Value of variable $RATED_TRQ'''
		return self._instance.RatedTrq

	@property
	def limit_func(self) -> int:
		'''Value of variable $LIMIT_FUNC'''
		return self._instance.LimitFunc

	@property
	def acc_lmt(self) -> typing.List[float]:
		'''Value of variable $ACC_LMT'''
		return self._instance.AccLmt

	@property
	def drive_type(self) -> typing.List[float]:
		'''Value of variable $DRIVE_TYPE'''
		return self._instance.DriveType

	@property
	def gear_ratio2(self) -> typing.List[float]:
		'''Value of variable $GEAR_RATIO2'''
		return self._instance.GearRatio2

	@property
	def dgclfr(self) -> typing.List[float]:
		'''Value of variable $DGCLFR'''
		return self._instance.Dgclfr

	@property
	def dgdyfr(self) -> typing.List[float]:
		'''Value of variable $DGDYFR'''
		return self._instance.Dgdyfr

	@property
	def dgldec(self) -> typing.List[float]:
		'''Value of variable $DGLDEC'''
		return self._instance.Dgldec

	@property
	def dg5t0(self) -> typing.List[float]:
		'''Value of variable $DG5T0'''
		return self._instance.Dg5t0

	@property
	def dg_maxt(self) -> typing.List[float]:
		'''Value of variable $DG_MAXT'''
		return self._instance.DgMaxt

	@property
	def dg_t0(self) -> typing.List[float]:
		'''Value of variable $DG_T0'''
		return self._instance.DgT0

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Fmr2GrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
