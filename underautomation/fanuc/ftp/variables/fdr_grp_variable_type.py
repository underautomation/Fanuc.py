import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FdrGrpVariableType as fdr_grp_variable_type

class FdrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type FDR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fdr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def vel_mod(self) -> typing.List[int]:
		'''Value of variable $VEL_MOD'''
		return self._instance.VelMod

	@property
	def vel_cnt(self) -> typing.List[int]:
		'''Value of variable $VEL_CNT'''
		return self._instance.VelCnt

	@property
	def rem_life2(self) -> typing.List[float]:
		'''Value of variable $REM_LIFE2'''
		return self._instance.RemLife2

	@property
	def ovm_rate(self) -> typing.List[float]:
		'''Value of variable $OVM_RATE'''
		return self._instance.OvmRate

	@property
	def ova_rate(self) -> typing.List[float]:
		'''Value of variable $OVA_RATE'''
		return self._instance.OvaRate

	@property
	def trov_rate(self) -> typing.List[float]:
		'''Value of variable $TROV_RATE'''
		return self._instance.TrovRate

	@property
	def dtav_rate(self) -> typing.List[float]:
		'''Value of variable $DTAV_RATE'''
		return self._instance.DtavRate

	@property
	def dtmx_rate(self) -> typing.List[float]:
		'''Value of variable $DTMX_RATE'''
		return self._instance.DtmxRate

	@property
	def dtmin_rate(self) -> typing.List[float]:
		'''Value of variable $DTMIN_RATE'''
		return self._instance.DtminRate

	@property
	def mot_rate(self) -> typing.List[float]:
		'''Value of variable $MOT_RATE'''
		return self._instance.MotRate

	@property
	def diag_indx_r(self) -> typing.List[float]:
		'''Value of variable $DIAG_INDX_R'''
		return self._instance.DiagIndxR

	@property
	def diag_indx_i(self) -> typing.List[int]:
		'''Value of variable $DIAG_INDX_I'''
		return self._instance.DiagIndxI

	@property
	def dg_maxt(self) -> typing.List[float]:
		'''Value of variable $DG_MAXT'''
		return self._instance.DgMaxt

	@property
	def dg_t0(self) -> typing.List[float]:
		'''Value of variable $DG_T0'''
		return self._instance.DgT0

	@property
	def rated_trq(self) -> typing.List[float]:
		'''Value of variable $RATED_TRQ'''
		return self._instance.RatedTrq

	@property
	def drive_type(self) -> typing.List[float]:
		'''Value of variable $DRIVE_TYPE'''
		return self._instance.DriveType

	@property
	def gear_ratio2(self) -> typing.List[float]:
		'''Value of variable $GEAR_RATIO2'''
		return self._instance.GearRatio2

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
	def z_mcmd(self) -> typing.List[int]:
		'''Value of variable $Z_MCMD'''
		return self._instance.ZMcmd

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FdrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
