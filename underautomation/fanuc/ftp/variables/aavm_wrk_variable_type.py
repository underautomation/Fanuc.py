import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AavmWrkVariableType as aavm_wrk_variable_type

class AavmWrkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavm_wrk_variable_type()
		else:
			self._instance = _internal
	@property
	def exposure(self) -> int:
		return self._instance.Exposure
	@property
	def camclbdate(self) -> str:
		return self._instance.Camclbdate
	@property
	def trgvt(self) -> float:
		return self._instance.Trgvt
	@property
	def trghz(self) -> float:
		return self._instance.Trghz
	@property
	def trgdist(self) -> float:
		return self._instance.Trgdist
	@property
	def trgw(self) -> float:
		return self._instance.Trgw
	@property
	def trgp(self) -> float:
		return self._instance.Trgp
	@property
	def trgr(self) -> float:
		return self._instance.Trgr
	@property
	def lens_cent_x(self) -> float:
		return self._instance.LensCentX
	@property
	def lens_cent_y(self) -> float:
		return self._instance.LensCentY
	@property
	def distort(self) -> typing.List[float]:
		return self._instance.Distort
	@property
	def cmp_gc_p(self) -> float:
		return self._instance.CmpGcP
	@property
	def utnum(self) -> int:
		return self._instance.Utnum
	@property
	def pre_mast_ct(self) -> typing.List[int]:
		return self._instance.PreMastCt
	@property
	def pre_grv_mst(self) -> int:
		return self._instance.PreGrvMst
	@property
	def new_mast_ct(self) -> typing.List[int]:
		return self._instance.NewMastCt
	@property
	def new_grv_mst(self) -> int:
		return self._instance.NewGrvMst
	@property
	def stat_run(self) -> int:
		return self._instance.StatRun
	@property
	def res_err(self) -> float:
		return self._instance.ResErr
	@property
	def vtcp_err(self) -> typing.List[float]:
		return self._instance.VtcpErr
	@property
	def trgt_err(self) -> typing.List[float]:
		return self._instance.TrgtErr
	@property
	def res_err2(self) -> float:
		return self._instance.ResErr2
	@property
	def vtcp_err2(self) -> typing.List[float]:
		return self._instance.VtcpErr2
	@property
	def rsm_mast_ct(self) -> typing.List[int]:
		return self._instance.RsmMastCt
	@property
	def stat_start(self) -> int:
		return self._instance.StatStart
	@property
	def stat_end(self) -> int:
		return self._instance.StatEnd
	@property
	def stat_orgbk(self) -> int:
		return self._instance.StatOrgbk
	@property
	def stat_rsmbk(self) -> int:
		return self._instance.StatRsmbk
	@property
	def stat_orgres(self) -> int:
		return self._instance.StatOrgres
	@property
	def stat_updt(self) -> int:
		return self._instance.StatUpdt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
