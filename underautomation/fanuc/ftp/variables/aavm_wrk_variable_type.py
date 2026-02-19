import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AavmWrkVariableType as aavm_wrk_variable_type

class AavmWrkVariableType(GenericVariableType):
	'''Describes the Fanuc type AAVM_WRK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavm_wrk_variable_type()
		else:
			self._instance = _internal

	@property
	def exposure(self) -> int:
		'''Value of variable $EXPOSURE'''
		return self._instance.Exposure

	@property
	def camclbdate(self) -> str:
		'''Value of variable $CAMCLBDATE'''
		return self._instance.Camclbdate

	@property
	def trgvt(self) -> float:
		'''Value of variable $TRGVT'''
		return self._instance.Trgvt

	@property
	def trghz(self) -> float:
		'''Value of variable $TRGHZ'''
		return self._instance.Trghz

	@property
	def trgdist(self) -> float:
		'''Value of variable $TRGDIST'''
		return self._instance.Trgdist

	@property
	def trgw(self) -> float:
		'''Value of variable $TRGW'''
		return self._instance.Trgw

	@property
	def trgp(self) -> float:
		'''Value of variable $TRGP'''
		return self._instance.Trgp

	@property
	def trgr(self) -> float:
		'''Value of variable $TRGR'''
		return self._instance.Trgr

	@property
	def lens_cent_x(self) -> float:
		'''Value of variable $LENS_CENT_X'''
		return self._instance.LensCentX

	@property
	def lens_cent_y(self) -> float:
		'''Value of variable $LENS_CENT_Y'''
		return self._instance.LensCentY

	@property
	def distort(self) -> typing.List[float]:
		'''Value of variable $DISTORT'''
		return self._instance.Distort

	@property
	def cmp_gc_p(self) -> float:
		'''Value of variable $CMP_GC_P'''
		return self._instance.CmpGcP

	@property
	def utnum(self) -> int:
		'''Value of variable $UTNUM'''
		return self._instance.Utnum

	@property
	def pre_mast_ct(self) -> typing.List[int]:
		'''Value of variable $PRE_MAST_CT'''
		return self._instance.PreMastCt

	@property
	def pre_grv_mst(self) -> int:
		'''Value of variable $PRE_GRV_MST'''
		return self._instance.PreGrvMst

	@property
	def new_mast_ct(self) -> typing.List[int]:
		'''Value of variable $NEW_MAST_CT'''
		return self._instance.NewMastCt

	@property
	def new_grv_mst(self) -> int:
		'''Value of variable $NEW_GRV_MST'''
		return self._instance.NewGrvMst

	@property
	def stat_run(self) -> int:
		'''Value of variable $STAT_RUN'''
		return self._instance.StatRun

	@property
	def res_err(self) -> float:
		'''Value of variable $RES_ERR'''
		return self._instance.ResErr

	@property
	def vtcp_err(self) -> typing.List[float]:
		'''Value of variable $VTCP_ERR'''
		return self._instance.VtcpErr

	@property
	def trgt_err(self) -> typing.List[float]:
		'''Value of variable $TRGT_ERR'''
		return self._instance.TrgtErr

	@property
	def res_err2(self) -> float:
		'''Value of variable $RES_ERR2'''
		return self._instance.ResErr2

	@property
	def vtcp_err2(self) -> typing.List[float]:
		'''Value of variable $VTCP_ERR2'''
		return self._instance.VtcpErr2

	@property
	def rsm_mast_ct(self) -> typing.List[int]:
		'''Value of variable $RSM_MAST_CT'''
		return self._instance.RsmMastCt

	@property
	def stat_start(self) -> int:
		'''Value of variable $STAT_START'''
		return self._instance.StatStart

	@property
	def stat_end(self) -> int:
		'''Value of variable $STAT_END'''
		return self._instance.StatEnd

	@property
	def stat_orgbk(self) -> int:
		'''Value of variable $STAT_ORGBK'''
		return self._instance.StatOrgbk

	@property
	def stat_rsmbk(self) -> int:
		'''Value of variable $STAT_RSMBK'''
		return self._instance.StatRsmbk

	@property
	def stat_orgres(self) -> int:
		'''Value of variable $STAT_ORGRES'''
		return self._instance.StatOrgres

	@property
	def stat_updt(self) -> int:
		'''Value of variable $STAT_UPDT'''
		return self._instance.StatUpdt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AavmWrkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
