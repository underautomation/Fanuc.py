import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcwmGrpVariableType as vcwm_grp_variable_type

class VcwmGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcwm_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def status_flag(self) -> int:
		return self._instance.StatusFlag
	@property
	def debug_mode(self) -> int:
		return self._instance.DebugMode
	@property
	def group_num(self) -> int:
		return self._instance.GroupNum
	@property
	def menu_code(self) -> int:
		return self._instance.MenuCode
	@property
	def num_mep(self) -> int:
		return self._instance.NumMep
	@property
	def num_retry(self) -> int:
		return self._instance.NumRetry
	@property
	def num_mep_usb(self) -> int:
		return self._instance.NumMepUsb
	@property
	def expos_time(self) -> int:
		return self._instance.ExposTime
	@property
	def trim_ratio(self) -> float:
		return self._instance.TrimRatio
	@property
	def camera_name(self) -> str:
		return self._instance.CameraName
	@property
	def tool_type(self) -> int:
		return self._instance.ToolType
	@property
	def focal_dist(self) -> float:
		return self._instance.FocalDist
	@property
	def grid_spacin(self) -> float:
		return self._instance.GridSpacin
	@property
	def swing_ang_d(self) -> typing.List[float]:
		return self._instance.SwingAngD
	@property
	def utool(self) -> typing.List[float]:
		return self._instance.Utool
	@property
	def upper_lim_s(self) -> float:
		return self._instance.UpperLimS
	@property
	def base_ang_d(self) -> typing.List[float]:
		return self._instance.BaseAngD
	@property
	def ang_range_d(self) -> typing.List[float]:
		return self._instance.AngRangeD
	@property
	def ini_pos_jnt(self) -> typing.List[float]:
		return self._instance.IniPosJnt
	@property
	def ref_pos_jnt(self) -> typing.List[float]:
		return self._instance.RefPosJnt
	@property
	def org_mst_ct(self) -> typing.List[int]:
		return self._instance.OrgMstCt
	@property
	def compe_ang_d(self) -> typing.List[float]:
		return self._instance.CompeAngD
	@property
	def new_mst_ct(self) -> typing.List[int]:
		return self._instance.NewMstCt
	@property
	def master_time(self) -> int:
		return self._instance.MasterTime
	@property
	def eval_index(self) -> float:
		return self._instance.EvalIndex
	@property
	def mean_res_er(self) -> float:
		return self._instance.MeanResEr
	@property
	def max_res_er(self) -> float:
		return self._instance.MaxResEr
	@property
	def trgt_pos_er(self) -> typing.List[float]:
		return self._instance.TrgtPosEr
	@property
	def worst_mp(self) -> int:
		return self._instance.WorstMp
	@property
	def move_xyz(self) -> float:
		return self._instance.MoveXyz
	@property
	def move_r_deg(self) -> float:
		return self._instance.MoveRDeg
	@property
	def log_port(self) -> int:
		return self._instance.LogPort
	@property
	def max_loop(self) -> int:
		return self._instance.MaxLoop
	@property
	def vfb_tol(self) -> float:
		return self._instance.VfbTol
	@property
	def vs_speed(self) -> float:
		return self._instance.VsSpeed
	@property
	def max_rdelay(self) -> int:
		return self._instance.MaxRdelay
	@property
	def pos_thres(self) -> float:
		return self._instance.PosThres
	@property
	def tilt_ang_d(self) -> float:
		return self._instance.TiltAngD
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
