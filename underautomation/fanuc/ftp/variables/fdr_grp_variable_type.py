import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FdrGrpVariableType as fdr_grp_variable_type

class FdrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fdr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def vel_mod(self) -> typing.List[int]:
		return self._instance.VelMod
	@property
	def vel_cnt(self) -> typing.List[int]:
		return self._instance.VelCnt
	@property
	def rem_life2(self) -> typing.List[float]:
		return self._instance.RemLife2
	@property
	def ovm_rate(self) -> typing.List[float]:
		return self._instance.OvmRate
	@property
	def ova_rate(self) -> typing.List[float]:
		return self._instance.OvaRate
	@property
	def trov_rate(self) -> typing.List[float]:
		return self._instance.TrovRate
	@property
	def dtav_rate(self) -> typing.List[float]:
		return self._instance.DtavRate
	@property
	def dtmx_rate(self) -> typing.List[float]:
		return self._instance.DtmxRate
	@property
	def dtmin_rate(self) -> typing.List[float]:
		return self._instance.DtminRate
	@property
	def mot_rate(self) -> typing.List[float]:
		return self._instance.MotRate
	@property
	def diag_indx_r(self) -> typing.List[float]:
		return self._instance.DiagIndxR
	@property
	def diag_indx_i(self) -> typing.List[int]:
		return self._instance.DiagIndxI
	@property
	def dg_maxt(self) -> typing.List[float]:
		return self._instance.DgMaxt
	@property
	def dg_t0(self) -> typing.List[float]:
		return self._instance.DgT0
	@property
	def rated_trq(self) -> typing.List[float]:
		return self._instance.RatedTrq
	@property
	def drive_type(self) -> typing.List[float]:
		return self._instance.DriveType
	@property
	def gear_ratio2(self) -> typing.List[float]:
		return self._instance.GearRatio2
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
	def z_mcmd(self) -> typing.List[int]:
		return self._instance.ZMcmd
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
