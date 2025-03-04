import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AavmGrpVariableType as aavm_grp_variable_type

class AavmGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavm_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def method_sel(self) -> int:
		return self._instance.MethodSel
	@property
	def focal_dist(self) -> float:
		return self._instance.FocalDist
	@property
	def gd_spacing(self) -> float:
		return self._instance.GdSpacing
	@property
	def offset_p(self) -> float:
		return self._instance.OffsetP
	@property
	def vtcp_des(self) -> typing.List[float]:
		return self._instance.VtcpDes
	@property
	def psshfenb(self) -> bool:
		return self._instance.Psshfenb
	@property
	def ps_shift(self) -> typing.List[float]:
		return self._instance.PsShift
	@property
	def ps_shiftj(self) -> float:
		return self._instance.PsShiftj
	@property
	def tagt_des(self) -> typing.List[float]:
		return self._instance.TagtDes
	@property
	def tagt_des2(self) -> typing.List[float]:
		return self._instance.TagtDes2
	@property
	def mast_axis(self) -> typing.List[float]:
		return self._instance.MastAxis
	@property
	def mast_axis2(self) -> typing.List[float]:
		return self._instance.MastAxis2
	@property
	def vfb_mat(self) -> typing.List[float]:
		return self._instance.VfbMat
	@property
	def num_pos(self) -> int:
		return self._instance.NumPos
	@property
	def num_pos2(self) -> int:
		return self._instance.NumPos2
	@property
	def mst_pos_x(self) -> typing.List[float]:
		return self._instance.MstPosX
	@property
	def mst_pos_y(self) -> typing.List[float]:
		return self._instance.MstPosY
	@property
	def mst_pos_z(self) -> typing.List[float]:
		return self._instance.MstPosZ
	@property
	def mst_pos_w(self) -> typing.List[float]:
		return self._instance.MstPosW
	@property
	def mst_pos_p(self) -> typing.List[float]:
		return self._instance.MstPosP
	@property
	def mst_pos_r(self) -> typing.List[float]:
		return self._instance.MstPosR
	@property
	def lim_res_er(self) -> float:
		return self._instance.LimResEr
	@property
	def lim_vtcp_x(self) -> float:
		return self._instance.LimVtcpX
	@property
	def lim_vtcp_z(self) -> float:
		return self._instance.LimVtcpZ
	@property
	def lim_tagt_x(self) -> float:
		return self._instance.LimTagtX
	@property
	def lim_tagt_z(self) -> float:
		return self._instance.LimTagtZ
	@property
	def vs_speed(self) -> float:
		return self._instance.VsSpeed
	@property
	def max_rdelay(self) -> int:
		return self._instance.MaxRdelay
	@property
	def vfa_tol1p(self) -> float:
		return self._instance.VfaTol1p
	@property
	def vfd_tol(self) -> float:
		return self._instance.VfdTol
	@property
	def vfd_tol1p(self) -> float:
		return self._instance.VfdTol1p
	@property
	def backlash(self) -> float:
		return self._instance.Backlash
	@property
	def limit_dx(self) -> float:
		return self._instance.LimitDx
	@property
	def limit_dy(self) -> float:
		return self._instance.LimitDy
	@property
	def limit_dz(self) -> float:
		return self._instance.LimitDz
	@property
	def limit_dw(self) -> float:
		return self._instance.LimitDw
	@property
	def limit_dp(self) -> float:
		return self._instance.LimitDp
	@property
	def limit_dr(self) -> float:
		return self._instance.LimitDr
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
	def camclbdate(self) -> str:
		return self._instance.Camclbdate
	@property
	def camera_name(self) -> str:
		return self._instance.CameraName
	@property
	def tool_type(self) -> int:
		return self._instance.ToolType
	@property
	def camera_type(self) -> int:
		return self._instance.CameraType
	@property
	def exposure(self) -> int:
		return self._instance.Exposure
	@property
	def num_mul_exp(self) -> int:
		return self._instance.NumMulExp
	@property
	def num_dovis(self) -> int:
		return self._instance.NumDovis
	@property
	def cmp_gc_w(self) -> float:
		return self._instance.CmpGcW
	@property
	def cmp_gc_p(self) -> float:
		return self._instance.CmpGcP
	@property
	def user_enb(self) -> bool:
		return self._instance.UserEnb
	@property
	def lim_res_er2(self) -> float:
		return self._instance.LimResEr2
	@property
	def lim_vtcp_x2(self) -> float:
		return self._instance.LimVtcpX2
	@property
	def lim_vtcp_z2(self) -> float:
		return self._instance.LimVtcpZ2
	@property
	def pre_ang(self) -> float:
		return self._instance.PreAng
	@property
	def pre_ang_j7(self) -> typing.List[float]:
		return self._instance.PreAngJ7
	@property
	def mst_pos_j7(self) -> typing.List[float]:
		return self._instance.MstPosJ7
	@property
	def trim_ratio(self) -> float:
		return self._instance.TrimRatio
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
