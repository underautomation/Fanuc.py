import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Fmr2GrpVariableType as fmr2_grp_variable_type

class Fmr2GrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fmr2_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def vel_rot(self) -> float:
		return self._instance.VelRot
	@property
	def vel_lin(self) -> float:
		return self._instance.VelLin
	@property
	def vel_mod(self) -> typing.List[int]:
		return self._instance.VelMod
	@property
	def k_life(self) -> typing.List[float]:
		return self._instance.KLife
	@property
	def ntr_life(self) -> typing.List[float]:
		return self._instance.NtrLife
	@property
	def eff_rate(self) -> typing.List[float]:
		return self._instance.EffRate
	@property
	def rot_inrt(self) -> typing.List[float]:
		return self._instance.RotInrt
	@property
	def trov_max(self) -> typing.List[float]:
		return self._instance.TrovMax
	@property
	def t_life0(self) -> float:
		return self._instance.TLife0
	@property
	def rated_trq(self) -> typing.List[float]:
		return self._instance.RatedTrq
	@property
	def limit_func(self) -> int:
		return self._instance.LimitFunc
	@property
	def acc_lmt(self) -> typing.List[float]:
		return self._instance.AccLmt
	@property
	def drive_type(self) -> typing.List[float]:
		return self._instance.DriveType
	@property
	def gear_ratio2(self) -> typing.List[float]:
		return self._instance.GearRatio2
	@property
	def dgclfr(self) -> typing.List[float]:
		return self._instance.Dgclfr
	@property
	def dgdyfr(self) -> typing.List[float]:
		return self._instance.Dgdyfr
	@property
	def dgldec(self) -> typing.List[float]:
		return self._instance.Dgldec
	@property
	def dg5t0(self) -> typing.List[float]:
		return self._instance.Dg5t0
	@property
	def dg_maxt(self) -> typing.List[float]:
		return self._instance.DgMaxt
	@property
	def dg_t0(self) -> typing.List[float]:
		return self._instance.DgT0
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
