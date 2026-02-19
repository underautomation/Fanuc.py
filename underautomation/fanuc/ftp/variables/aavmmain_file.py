import typing
from underautomation.fanuc.ftp.variables.aavm_grp_variable_type import AavmGrpVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import AavmmainFile as aavmmain_file

class AavmmainFile(GenericVariableFile):
	'''Describes the Fanuc variable file aavmmain.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavmmain_file()
		else:
			self._instance = _internal

	@property
	def i(self) -> int:
		'''Value of variable I'''
		return self._instance.I

	@property
	def rob_grp(self) -> int:
		'''Value of variable ROB_GRP'''
		return self._instance.RobGrp

	@property
	def num_axis(self) -> int:
		'''Value of variable NUM_AXIS'''
		return self._instance.NumAxis

	@property
	def prm(self) -> AavmGrpVariableType:
		'''Value of variable PRM'''
		return AavmGrpVariableType(self._instance.Prm)

	@property
	def ps_rob_grp(self) -> int:
		'''Value of variable PS_ROB_GRP'''
		return self._instance.PsRobGrp

	@property
	def cond_num(self) -> float:
		'''Value of variable COND_NUM'''
		return self._instance.CondNum

	@property
	def res_err(self) -> float:
		'''Value of variable RES_ERR'''
		return self._instance.ResErr

	@property
	def res_err_str(self) -> str:
		'''Value of variable RES_ERR_STR'''
		return self._instance.ResErrStr

	@property
	def param_name(self) -> str:
		'''Value of variable PARAM_NAME'''
		return self._instance.ParamName

	@property
	def data_type(self) -> int:
		'''Value of variable DATA_TYPE'''
		return self._instance.DataType

	@property
	def dmy_int(self) -> int:
		'''Value of variable DMY_INT'''
		return self._instance.DmyInt

	@property
	def dmy_real(self) -> float:
		'''Value of variable DMY_REAL'''
		return self._instance.DmyReal

	@property
	def dmy_str(self) -> str:
		'''Value of variable DMY_STR'''
		return self._instance.DmyStr

	@property
	def dmy_str2(self) -> str:
		'''Value of variable DMY_STR2'''
		return self._instance.DmyStr2

	@property
	def dmy_stat(self) -> int:
		'''Value of variable DMY_STAT'''
		return self._instance.DmyStat

	@property
	def vfb_mat(self) -> typing.List[float]:
		'''Value of variable VFB_MAT'''
		return self._instance.VfbMat

	@property
	def res_err1(self) -> float:
		'''Value of variable RES_ERR1'''
		return self._instance.ResErr1

	@property
	def res_er1_thsd(self) -> float:
		'''Value of variable RES_ER1_THSD'''
		return self._instance.ResEr1Thsd

	@property
	def vtcp_x1_thsd(self) -> float:
		'''Value of variable VTCP_X1_THSD'''
		return self._instance.VtcpX1Thsd

	@property
	def vtcp_z1_thsd(self) -> float:
		'''Value of variable VTCP_Z1_THSD'''
		return self._instance.VtcpZ1Thsd

	@property
	def tagt_x1_thsd(self) -> float:
		'''Value of variable TAGT_X1_THSD'''
		return self._instance.TagtX1Thsd

	@property
	def tagt_z1_thsd(self) -> float:
		'''Value of variable TAGT_Z1_THSD'''
		return self._instance.TagtZ1Thsd

	@property
	def res_err2(self) -> float:
		'''Value of variable RES_ERR2'''
		return self._instance.ResErr2

	@property
	def res_er2_thsd(self) -> float:
		'''Value of variable RES_ER2_THSD'''
		return self._instance.ResEr2Thsd

	@property
	def vtcp_x2_thsd(self) -> float:
		'''Value of variable VTCP_X2_THSD'''
		return self._instance.VtcpX2Thsd

	@property
	def vtcp_z2_thsd(self) -> float:
		'''Value of variable VTCP_Z2_THSD'''
		return self._instance.VtcpZ2Thsd

	@property
	def tagt_x2_thsd(self) -> float:
		'''Value of variable TAGT_X2_THSD'''
		return self._instance.TagtX2Thsd

	@property
	def tagt_z2_thsd(self) -> float:
		'''Value of variable TAGT_Z2_THSD'''
		return self._instance.TagtZ2Thsd

	@property
	def device(self) -> int:
		'''Value of variable DEVICE'''
		return self._instance.Device

	@property
	def file_name(self) -> str:
		'''Value of variable FILE_NAME'''
		return self._instance.FileName

	@property
	def log_port(self) -> int:
		'''Value of variable LOG_PORT'''
		return self._instance.LogPort

	@property
	def aavm_step(self) -> int:
		'''Value of variable AAVM_STEP'''
		return self._instance.AavmStep

	@property
	def mast_coun0(self) -> typing.List[int]:
		'''Value of variable MAST_COUN0'''
		return self._instance.MastCoun0

	@property
	def mast_coun02(self) -> typing.List[int]:
		'''Value of variable MAST_COUN0_2'''
		return self._instance.MastCoun02

	@property
	def ext_mct0(self) -> typing.List[int]:
		'''Value of variable EXT_MCT0'''
		return self._instance.ExtMct0

	@property
	def jpos_data(self) -> typing.List[float]:
		'''Value of variable JPOS_DATA'''
		return self._instance.JposData

	@property
	def vtcp(self) -> CartesianPositionVariable:
		'''Value of variable VTCP'''
		return CartesianPositionVariable(self._instance.Vtcp)

	@property
	def vtcp0(self) -> CartesianPositionVariable:
		'''Value of variable VTCP0'''
		return CartesianPositionVariable(self._instance.Vtcp0)

	@property
	def target(self) -> CartesianPositionVariable:
		'''Value of variable TARGET'''
		return CartesianPositionVariable(self._instance.Target)

	@property
	def target0(self) -> CartesianPositionVariable:
		'''Value of variable TARGET0'''
		return CartesianPositionVariable(self._instance.Target0)

	@property
	def cmp_jpos(self) -> typing.List[float]:
		'''Value of variable CMP_JPOS'''
		return self._instance.CmpJpos

	@property
	def mast_axis(self) -> typing.List[float]:
		'''Value of variable MAST_AXIS'''
		return self._instance.MastAxis

	@property
	def tmp_axis(self) -> typing.List[float]:
		'''Value of variable TMP_AXIS'''
		return self._instance.TmpAxis

	@property
	def er_vtcpx(self) -> float:
		'''Value of variable ER_VTCPX'''
		return self._instance.ErVtcpx

	@property
	def er_vtcpz(self) -> float:
		'''Value of variable ER_VTCPZ'''
		return self._instance.ErVtcpz

	@property
	def er_targtx(self) -> float:
		'''Value of variable ER_TARGTX'''
		return self._instance.ErTargtx

	@property
	def er_targty(self) -> float:
		'''Value of variable ER_TARGTY'''
		return self._instance.ErTargty

	@property
	def er_targtz(self) -> float:
		'''Value of variable ER_TARGTZ'''
		return self._instance.ErTargtz

	@property
	def er_vtcpx1(self) -> float:
		'''Value of variable ER_VTCPX1'''
		return self._instance.ErVtcpx1

	@property
	def er_vtcpz1(self) -> float:
		'''Value of variable ER_VTCPZ1'''
		return self._instance.ErVtcpz1

	@property
	def er_targtx1(self) -> float:
		'''Value of variable ER_TARGTX1'''
		return self._instance.ErTargtx1

	@property
	def er_targtz1(self) -> float:
		'''Value of variable ER_TARGTZ1'''
		return self._instance.ErTargtz1

	@property
	def er_vtcpx2(self) -> float:
		'''Value of variable ER_VTCPX2'''
		return self._instance.ErVtcpx2

	@property
	def er_vtcpz2(self) -> float:
		'''Value of variable ER_VTCPZ2'''
		return self._instance.ErVtcpz2

	@property
	def er_targtx2(self) -> float:
		'''Value of variable ER_TARGTX2'''
		return self._instance.ErTargtx2

	@property
	def er_targtz2(self) -> float:
		'''Value of variable ER_TARGTZ2'''
		return self._instance.ErTargtz2

	@property
	def meas_pose(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable MEAS_POSE'''
		return [CartesianPositionVariable(x) for x in self._instance.MeasPose]

	@property
	def dual_num(self) -> int:
		'''Value of variable DUAL_NUM'''
		return self._instance.DualNum

	@property
	def s_axis_num(self) -> int:
		'''Value of variable S_AXIS_NUM'''
		return self._instance.SAxisNum

	@property
	def tpp_run(self) -> bool:
		'''Value of variable TPP_RUN'''
		return self._instance.TppRun

	@property
	def step_su1(self) -> int:
		'''Value of variable STEP_SU1'''
		return self._instance.StepSu1

	@property
	def step_su2(self) -> int:
		'''Value of variable STEP_SU2'''
		return self._instance.StepSu2

	@property
	def step_su3(self) -> int:
		'''Value of variable STEP_SU3'''
		return self._instance.StepSu3

	@property
	def step_su4(self) -> int:
		'''Value of variable STEP_SU4'''
		return self._instance.StepSu4

	@property
	def min_num_dots(self) -> int:
		'''Value of variable MIN_NUM_DOTS'''
		return self._instance.MinNumDots

	@property
	def pix_size_low(self) -> float:
		'''Value of variable PIX_SIZE_LOW'''
		return self._instance.PixSizeLow

	@property
	def pix_siz_high(self) -> float:
		'''Value of variable PIX_SIZ_HIGH'''
		return self._instance.PixSizHigh

	@property
	def aspect_low(self) -> float:
		'''Value of variable ASPECT_LOW'''
		return self._instance.AspectLow

	@property
	def is_autoexpo(self) -> bool:
		'''Value of variable IS_AUTOEXPO'''
		return self._instance.IsAutoexpo

	@property
	def ae_cont_low(self) -> int:
		'''Value of variable AE_CONT_LOW'''
		return self._instance.AeContLow

	@property
	def ae_cont_ave(self) -> int:
		'''Value of variable AE_CONT_AVE'''
		return self._instance.AeContAve

	@property
	def ae_num_retry(self) -> int:
		'''Value of variable AE_NUM_RETRY'''
		return self._instance.AeNumRetry

	@property
	def ae_radi_ratio(self) -> float:
		'''Value of variable AE_RADI_RATIO'''
		return self._instance.AeRadiRatio

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AavmmainFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
