import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcwmGrpVariableType as vcwm_grp_variable_type

class VcwmGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type VCWM_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcwm_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def status_flag(self) -> int:
		'''Value of variable $STATUS_FLAG'''
		return self._instance.StatusFlag

	@property
	def debug_mode(self) -> int:
		'''Value of variable $DEBUG_MODE'''
		return self._instance.DebugMode

	@property
	def group_num(self) -> int:
		'''Value of variable $GROUP_NUM'''
		return self._instance.GroupNum

	@property
	def menu_code(self) -> int:
		'''Value of variable $MENU_CODE'''
		return self._instance.MenuCode

	@property
	def num_mep(self) -> int:
		'''Value of variable $NUM_MEP'''
		return self._instance.NumMep

	@property
	def num_retry(self) -> int:
		'''Value of variable $NUM_RETRY'''
		return self._instance.NumRetry

	@property
	def num_mep_usb(self) -> int:
		'''Value of variable $NUM_MEP_USB'''
		return self._instance.NumMepUsb

	@property
	def expos_time(self) -> int:
		'''Value of variable $EXPOS_TIME'''
		return self._instance.ExposTime

	@property
	def trim_ratio(self) -> float:
		'''Value of variable $TRIM_RATIO'''
		return self._instance.TrimRatio

	@property
	def camera_name(self) -> str:
		'''Value of variable $CAMERA_NAME'''
		return self._instance.CameraName

	@property
	def tool_type(self) -> int:
		'''Value of variable $TOOL_TYPE'''
		return self._instance.ToolType

	@property
	def focal_dist(self) -> float:
		'''Value of variable $FOCAL_DIST'''
		return self._instance.FocalDist

	@property
	def grid_spacin(self) -> float:
		'''Value of variable $GRID_SPACIN'''
		return self._instance.GridSpacin

	@property
	def swing_ang_d(self) -> typing.List[float]:
		'''Value of variable $SWING_ANG_D'''
		return self._instance.SwingAngD

	@property
	def utool(self) -> typing.List[float]:
		'''Value of variable $UTOOL'''
		return self._instance.Utool

	@property
	def upper_lim_s(self) -> float:
		'''Value of variable $UPPER_LIM_S'''
		return self._instance.UpperLimS

	@property
	def base_ang_d(self) -> typing.List[float]:
		'''Value of variable $BASE_ANG_D'''
		return self._instance.BaseAngD

	@property
	def ang_range_d(self) -> typing.List[float]:
		'''Value of variable $ANG_RANGE_D'''
		return self._instance.AngRangeD

	@property
	def ini_pos_jnt(self) -> typing.List[float]:
		'''Value of variable $INI_POS_JNT'''
		return self._instance.IniPosJnt

	@property
	def ref_pos_jnt(self) -> typing.List[float]:
		'''Value of variable $REF_POS_JNT'''
		return self._instance.RefPosJnt

	@property
	def org_mst_ct(self) -> typing.List[int]:
		'''Value of variable $ORG_MST_CT'''
		return self._instance.OrgMstCt

	@property
	def compe_ang_d(self) -> typing.List[float]:
		'''Value of variable $COMPE_ANG_D'''
		return self._instance.CompeAngD

	@property
	def new_mst_ct(self) -> typing.List[int]:
		'''Value of variable $NEW_MST_CT'''
		return self._instance.NewMstCt

	@property
	def master_time(self) -> int:
		'''Value of variable $MASTER_TIME'''
		return self._instance.MasterTime

	@property
	def eval_index(self) -> float:
		'''Value of variable $EVAL_INDEX'''
		return self._instance.EvalIndex

	@property
	def mean_res_er(self) -> float:
		'''Value of variable $MEAN_RES_ER'''
		return self._instance.MeanResEr

	@property
	def max_res_er(self) -> float:
		'''Value of variable $MAX_RES_ER'''
		return self._instance.MaxResEr

	@property
	def trgt_pos_er(self) -> typing.List[float]:
		'''Value of variable $TRGT_POS_ER'''
		return self._instance.TrgtPosEr

	@property
	def worst_mp(self) -> int:
		'''Value of variable $WORST_MP'''
		return self._instance.WorstMp

	@property
	def move_xyz(self) -> float:
		'''Value of variable $MOVE_XYZ'''
		return self._instance.MoveXyz

	@property
	def move_r_deg(self) -> float:
		'''Value of variable $MOVE_R_DEG'''
		return self._instance.MoveRDeg

	@property
	def log_port(self) -> int:
		'''Value of variable $LOG_PORT'''
		return self._instance.LogPort

	@property
	def max_loop(self) -> int:
		'''Value of variable $MAX_LOOP'''
		return self._instance.MaxLoop

	@property
	def vfb_tol(self) -> float:
		'''Value of variable $VFB_TOL'''
		return self._instance.VfbTol

	@property
	def vs_speed(self) -> float:
		'''Value of variable $VS_SPEED'''
		return self._instance.VsSpeed

	@property
	def max_rdelay(self) -> int:
		'''Value of variable $MAX_RDELAY'''
		return self._instance.MaxRdelay

	@property
	def pos_thres(self) -> float:
		'''Value of variable $POS_THRES'''
		return self._instance.PosThres

	@property
	def tilt_ang_d(self) -> float:
		'''Value of variable $TILT_ANG_D'''
		return self._instance.TiltAngD

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcwmGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
