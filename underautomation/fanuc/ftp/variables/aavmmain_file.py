import typing
from underautomation.fanuc.ftp.variables.aavm_grp_variable_type import AavmGrpVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AavmmainFile as aavmmain_file

class AavmmainFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aavmmain_file()
		else:
			self._instance = _internal
	@property
	def i(self) -> int:
		return self._instance.I
	@property
	def rob_grp(self) -> int:
		return self._instance.RobGrp
	@property
	def num_axis(self) -> int:
		return self._instance.NumAxis
	@property
	def prm(self) -> AavmGrpVariableType:
		return AavmGrpVariableType(self._instance.Prm)
	@property
	def ps_rob_grp(self) -> int:
		return self._instance.PsRobGrp
	@property
	def cond_num(self) -> float:
		return self._instance.CondNum
	@property
	def res_err(self) -> float:
		return self._instance.ResErr
	@property
	def res_err_str(self) -> str:
		return self._instance.ResErrStr
	@property
	def param_name(self) -> str:
		return self._instance.ParamName
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def dmy_int(self) -> int:
		return self._instance.DmyInt
	@property
	def dmy_real(self) -> float:
		return self._instance.DmyReal
	@property
	def dmy_str(self) -> str:
		return self._instance.DmyStr
	@property
	def dmy_str2(self) -> str:
		return self._instance.DmyStr2
	@property
	def dmy_stat(self) -> int:
		return self._instance.DmyStat
	@property
	def vfb_mat(self) -> typing.List[float]:
		return self._instance.VfbMat
	@property
	def res_err1(self) -> float:
		return self._instance.ResErr1
	@property
	def res_er1_thsd(self) -> float:
		return self._instance.ResEr1Thsd
	@property
	def vtcp_x1_thsd(self) -> float:
		return self._instance.VtcpX1Thsd
	@property
	def vtcp_z1_thsd(self) -> float:
		return self._instance.VtcpZ1Thsd
	@property
	def tagt_x1_thsd(self) -> float:
		return self._instance.TagtX1Thsd
	@property
	def tagt_z1_thsd(self) -> float:
		return self._instance.TagtZ1Thsd
	@property
	def res_err2(self) -> float:
		return self._instance.ResErr2
	@property
	def res_er2_thsd(self) -> float:
		return self._instance.ResEr2Thsd
	@property
	def vtcp_x2_thsd(self) -> float:
		return self._instance.VtcpX2Thsd
	@property
	def vtcp_z2_thsd(self) -> float:
		return self._instance.VtcpZ2Thsd
	@property
	def tagt_x2_thsd(self) -> float:
		return self._instance.TagtX2Thsd
	@property
	def tagt_z2_thsd(self) -> float:
		return self._instance.TagtZ2Thsd
	@property
	def device(self) -> int:
		return self._instance.Device
	@property
	def file_name(self) -> str:
		return self._instance.FileName
	@property
	def log_port(self) -> int:
		return self._instance.LogPort
	@property
	def aavm_step(self) -> int:
		return self._instance.AavmStep
	@property
	def mast_coun0(self) -> typing.List[int]:
		return self._instance.MastCoun0
	@property
	def mast_coun02(self) -> typing.List[int]:
		return self._instance.MastCoun02
	@property
	def ext_mct0(self) -> typing.List[int]:
		return self._instance.ExtMct0
	@property
	def jpos_data(self) -> typing.List[float]:
		return self._instance.JposData
	@property
	def vtcp(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Vtcp)
	@property
	def vtcp0(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Vtcp0)
	@property
	def target(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Target)
	@property
	def target0(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Target0)
	@property
	def cmp_jpos(self) -> typing.List[float]:
		return self._instance.CmpJpos
	@property
	def mast_axis(self) -> typing.List[float]:
		return self._instance.MastAxis
	@property
	def tmp_axis(self) -> typing.List[float]:
		return self._instance.TmpAxis
	@property
	def er_vtcpx(self) -> float:
		return self._instance.ErVtcpx
	@property
	def er_vtcpz(self) -> float:
		return self._instance.ErVtcpz
	@property
	def er_targtx(self) -> float:
		return self._instance.ErTargtx
	@property
	def er_targty(self) -> float:
		return self._instance.ErTargty
	@property
	def er_targtz(self) -> float:
		return self._instance.ErTargtz
	@property
	def er_vtcpx1(self) -> float:
		return self._instance.ErVtcpx1
	@property
	def er_vtcpz1(self) -> float:
		return self._instance.ErVtcpz1
	@property
	def er_targtx1(self) -> float:
		return self._instance.ErTargtx1
	@property
	def er_targtz1(self) -> float:
		return self._instance.ErTargtz1
	@property
	def er_vtcpx2(self) -> float:
		return self._instance.ErVtcpx2
	@property
	def er_vtcpz2(self) -> float:
		return self._instance.ErVtcpz2
	@property
	def er_targtx2(self) -> float:
		return self._instance.ErTargtx2
	@property
	def er_targtz2(self) -> float:
		return self._instance.ErTargtz2
	@property
	def meas_pose(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.MeasPose]
	@property
	def dual_num(self) -> int:
		return self._instance.DualNum
	@property
	def s_axis_num(self) -> int:
		return self._instance.SAxisNum
	@property
	def tpp_run(self) -> bool:
		return self._instance.TppRun
	@property
	def step_su1(self) -> int:
		return self._instance.StepSu1
	@property
	def step_su2(self) -> int:
		return self._instance.StepSu2
	@property
	def step_su3(self) -> int:
		return self._instance.StepSu3
	@property
	def step_su4(self) -> int:
		return self._instance.StepSu4
	@property
	def min_num_dots(self) -> int:
		return self._instance.MinNumDots
	@property
	def pix_size_low(self) -> float:
		return self._instance.PixSizeLow
	@property
	def pix_siz_high(self) -> float:
		return self._instance.PixSizHigh
	@property
	def aspect_low(self) -> float:
		return self._instance.AspectLow
	@property
	def is_autoexpo(self) -> bool:
		return self._instance.IsAutoexpo
	@property
	def ae_cont_low(self) -> int:
		return self._instance.AeContLow
	@property
	def ae_cont_ave(self) -> int:
		return self._instance.AeContAve
	@property
	def ae_num_retry(self) -> int:
		return self._instance.AeNumRetry
	@property
	def ae_radi_ratio(self) -> float:
		return self._instance.AeRadiRatio
