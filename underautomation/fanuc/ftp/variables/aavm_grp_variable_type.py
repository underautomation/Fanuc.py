import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AavmGrpVariableType as aavm_grp_variable_type

class AavmGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type AAVM_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavm_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def method_sel(self) -> int:
		'''Value of variable $METHOD_SEL'''
		return self._instance.MethodSel

	@property
	def focal_dist(self) -> float:
		'''Value of variable $FOCAL_DIST'''
		return self._instance.FocalDist

	@property
	def gd_spacing(self) -> float:
		'''Value of variable $GD_SPACING'''
		return self._instance.GdSpacing

	@property
	def offset_p(self) -> float:
		'''Value of variable $OFFSET_P'''
		return self._instance.OffsetP

	@property
	def vtcp_des(self) -> typing.List[float]:
		'''Value of variable $VTCP_DES'''
		return self._instance.VtcpDes

	@property
	def psshfenb(self) -> bool:
		'''Value of variable $PSSHFENB'''
		return self._instance.Psshfenb

	@property
	def ps_shift(self) -> typing.List[float]:
		'''Value of variable $PS_SHIFT'''
		return self._instance.PsShift

	@property
	def ps_shiftj(self) -> float:
		'''Value of variable $PS_SHIFTJ'''
		return self._instance.PsShiftj

	@property
	def tagt_des(self) -> typing.List[float]:
		'''Value of variable $TAGT_DES'''
		return self._instance.TagtDes

	@property
	def tagt_des2(self) -> typing.List[float]:
		'''Value of variable $TAGT_DES2'''
		return self._instance.TagtDes2

	@property
	def mast_axis(self) -> typing.List[float]:
		'''Value of variable $MAST_AXIS'''
		return self._instance.MastAxis

	@property
	def mast_axis2(self) -> typing.List[float]:
		'''Value of variable $MAST_AXIS2'''
		return self._instance.MastAxis2

	@property
	def vfb_mat(self) -> typing.List[float]:
		'''Value of variable $VFB_MAT'''
		return self._instance.VfbMat

	@property
	def num_pos(self) -> int:
		'''Value of variable $NUM_POS'''
		return self._instance.NumPos

	@property
	def num_pos2(self) -> int:
		'''Value of variable $NUM_POS2'''
		return self._instance.NumPos2

	@property
	def mst_pos_x(self) -> typing.List[float]:
		'''Value of variable $MST_POS_X'''
		return self._instance.MstPosX

	@property
	def mst_pos_y(self) -> typing.List[float]:
		'''Value of variable $MST_POS_Y'''
		return self._instance.MstPosY

	@property
	def mst_pos_z(self) -> typing.List[float]:
		'''Value of variable $MST_POS_Z'''
		return self._instance.MstPosZ

	@property
	def mst_pos_w(self) -> typing.List[float]:
		'''Value of variable $MST_POS_W'''
		return self._instance.MstPosW

	@property
	def mst_pos_p(self) -> typing.List[float]:
		'''Value of variable $MST_POS_P'''
		return self._instance.MstPosP

	@property
	def mst_pos_r(self) -> typing.List[float]:
		'''Value of variable $MST_POS_R'''
		return self._instance.MstPosR

	@property
	def lim_res_er(self) -> float:
		'''Value of variable $LIM_RES_ER'''
		return self._instance.LimResEr

	@property
	def lim_vtcp_x(self) -> float:
		'''Value of variable $LIM_VTCP_X'''
		return self._instance.LimVtcpX

	@property
	def lim_vtcp_z(self) -> float:
		'''Value of variable $LIM_VTCP_Z'''
		return self._instance.LimVtcpZ

	@property
	def lim_tagt_x(self) -> float:
		'''Value of variable $LIM_TAGT_X'''
		return self._instance.LimTagtX

	@property
	def lim_tagt_z(self) -> float:
		'''Value of variable $LIM_TAGT_Z'''
		return self._instance.LimTagtZ

	@property
	def vs_speed(self) -> float:
		'''Value of variable $VS_SPEED'''
		return self._instance.VsSpeed

	@property
	def max_rdelay(self) -> int:
		'''Value of variable $MAX_RDELAY'''
		return self._instance.MaxRdelay

	@property
	def vfa_tol1p(self) -> float:
		'''Value of variable $VFA_TOL_1P'''
		return self._instance.VfaTol1p

	@property
	def vfd_tol(self) -> float:
		'''Value of variable $VFD_TOL'''
		return self._instance.VfdTol

	@property
	def vfd_tol1p(self) -> float:
		'''Value of variable $VFD_TOL_1P'''
		return self._instance.VfdTol1p

	@property
	def backlash(self) -> float:
		'''Value of variable $BACKLASH'''
		return self._instance.Backlash

	@property
	def limit_dx(self) -> float:
		'''Value of variable $LIMIT_DX'''
		return self._instance.LimitDx

	@property
	def limit_dy(self) -> float:
		'''Value of variable $LIMIT_DY'''
		return self._instance.LimitDy

	@property
	def limit_dz(self) -> float:
		'''Value of variable $LIMIT_DZ'''
		return self._instance.LimitDz

	@property
	def limit_dw(self) -> float:
		'''Value of variable $LIMIT_DW'''
		return self._instance.LimitDw

	@property
	def limit_dp(self) -> float:
		'''Value of variable $LIMIT_DP'''
		return self._instance.LimitDp

	@property
	def limit_dr(self) -> float:
		'''Value of variable $LIMIT_DR'''
		return self._instance.LimitDr

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
	def camclbdate(self) -> str:
		'''Value of variable $CAMCLBDATE'''
		return self._instance.Camclbdate

	@property
	def camera_name(self) -> str:
		'''Value of variable $CAMERA_NAME'''
		return self._instance.CameraName

	@property
	def tool_type(self) -> int:
		'''Value of variable $TOOL_TYPE'''
		return self._instance.ToolType

	@property
	def camera_type(self) -> int:
		'''Value of variable $CAMERA_TYPE'''
		return self._instance.CameraType

	@property
	def exposure(self) -> int:
		'''Value of variable $EXPOSURE'''
		return self._instance.Exposure

	@property
	def num_mul_exp(self) -> int:
		'''Value of variable $NUM_MUL_EXP'''
		return self._instance.NumMulExp

	@property
	def num_dovis(self) -> int:
		'''Value of variable $NUM_DOVIS'''
		return self._instance.NumDovis

	@property
	def cmp_gc_w(self) -> float:
		'''Value of variable $CMP_GC_W'''
		return self._instance.CmpGcW

	@property
	def cmp_gc_p(self) -> float:
		'''Value of variable $CMP_GC_P'''
		return self._instance.CmpGcP

	@property
	def user_enb(self) -> bool:
		'''Value of variable $USER_ENB'''
		return self._instance.UserEnb

	@property
	def lim_res_er2(self) -> float:
		'''Value of variable $LIM_RES_ER2'''
		return self._instance.LimResEr2

	@property
	def lim_vtcp_x2(self) -> float:
		'''Value of variable $LIM_VTCP_X2'''
		return self._instance.LimVtcpX2

	@property
	def lim_vtcp_z2(self) -> float:
		'''Value of variable $LIM_VTCP_Z2'''
		return self._instance.LimVtcpZ2

	@property
	def pre_ang(self) -> float:
		'''Value of variable $PRE_ANG'''
		return self._instance.PreAng

	@property
	def pre_ang_j7(self) -> typing.List[float]:
		'''Value of variable $PRE_ANG_J7'''
		return self._instance.PreAngJ7

	@property
	def mst_pos_j7(self) -> typing.List[float]:
		'''Value of variable $MST_POS_J7'''
		return self._instance.MstPosJ7

	@property
	def trim_ratio(self) -> float:
		'''Value of variable $TRIM_RATIO'''
		return self._instance.TrimRatio

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AavmGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
