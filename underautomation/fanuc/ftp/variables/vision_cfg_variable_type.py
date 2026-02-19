import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VisionCfgVariableType as vision_cfg_variable_type

class VisionCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type VISION_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vision_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def data_path(self) -> str:
		'''Value of variable $DATA_PATH'''
		return self._instance.DataPath

	@property
	def data_cache(self) -> int:
		'''Value of variable $DATA_CACHE'''
		return self._instance.DataCache

	@property
	def log_path(self) -> str:
		'''Value of variable $LOG_PATH'''
		return self._instance.LogPath

	@property
	def log_expath(self) -> str:
		'''Value of variable $LOG_EXPATH'''
		return self._instance.LogExpath

	@property
	def log_timeout(self) -> int:
		'''Value of variable $LOG_TIMEOUT'''
		return self._instance.LogTimeout

	@property
	def mc_limit(self) -> int:
		'''Value of variable $MC_LIMIT'''
		return self._instance.McLimit

	@property
	def fr_limit(self) -> int:
		'''Value of variable $FR_LIMIT'''
		return self._instance.FrLimit

	@property
	def td_limit(self) -> int:
		'''Value of variable $TD_LIMIT'''
		return self._instance.TdLimit

	@property
	def debug_mode(self) -> int:
		'''Value of variable $DEBUG_MODE'''
		return self._instance.DebugMode

	@property
	def host_name(self) -> str:
		'''Value of variable $HOST_NAME'''
		return self._instance.HostName

	@property
	def comm_port(self) -> int:
		'''Value of variable $COMM_PORT'''
		return self._instance.CommPort

	@property
	def robot_name(self) -> str:
		'''Value of variable $ROBOT_NAME'''
		return self._instance.RobotName

	@property
	def flags(self) -> int:
		'''Value of variable $FLAGS'''
		return self._instance.Flags

	@property
	def flags2(self) -> int:
		'''Value of variable $FLAGS2'''
		return self._instance.Flags2

	@property
	def max_pages(self) -> int:
		'''Value of variable $MAX_PAGES'''
		return self._instance.MaxPages

	@property
	def min_vpool(self) -> int:
		'''Value of variable $MIN_VPOOL'''
		return self._instance.MinVpool

	@property
	def vpool_size(self) -> int:
		'''Value of variable $VPOOL_SIZE'''
		return self._instance.VpoolSize

	@property
	def vpool_szcal(self) -> int:
		'''Value of variable $VPOOL_SZCAL'''
		return self._instance.VpoolSzcal

	@property
	def vpool_lim(self) -> int:
		'''Value of variable $VPOOL_LIM'''
		return self._instance.VpoolLim

	@property
	def vpool_wait(self) -> int:
		'''Value of variable $VPOOL_WAIT'''
		return self._instance.VpoolWait

	@property
	def tmppool_lim(self) -> int:
		'''Value of variable $TMPPOOL_LIM'''
		return self._instance.TmppoolLim

	@property
	def failimg_idx(self) -> int:
		'''Value of variable $FAILIMG_IDX'''
		return self._instance.FailimgIdx

	@property
	def loadimg_idx(self) -> int:
		'''Value of variable $LOADIMG_IDX'''
		return self._instance.LoadimgIdx

	@property
	def num_imregs(self) -> int:
		'''Value of variable $NUM_IMREGS'''
		return self._instance.NumImregs

	@property
	def imreg_size(self) -> int:
		'''Value of variable $IMREG_SIZE'''
		return self._instance.ImregSize

	@property
	def gpm_candmax(self) -> int:
		'''Value of variable $GPM_CANDMAX'''
		return self._instance.GpmCandmax

	@property
	def num_asynbuf(self) -> int:
		'''Value of variable $NUM_ASYNBUF'''
		return self._instance.NumAsynbuf

	@property
	def num_vrtdbuf(self) -> int:
		'''Value of variable $NUM_VRTDBUF'''
		return self._instance.NumVrtdbuf

	@property
	def vrtdbuf_siz(self) -> int:
		'''Value of variable $VRTDBUF_SIZ'''
		return self._instance.VrtdbufSiz

	@property
	def tole2d_z(self) -> float:
		'''Value of variable $TOLE_2D_Z'''
		return self._instance.Tole2dZ

	@property
	def tole2d_wp(self) -> float:
		'''Value of variable $TOLE_2D_WP'''
		return self._instance.Tole2dWp

	@property
	def pc_setup(self) -> bool:
		'''Value of variable $PC_SETUP'''
		return self._instance.PcSetup

	@property
	def logque_max(self) -> int:
		'''Value of variable $LOGQUE_MAX'''
		return self._instance.LogqueMax

	@property
	def eccu_retry(self) -> int:
		'''Value of variable $ECCU_RETRY'''
		return self._instance.EccuRetry

	@property
	def vemt_path(self) -> str:
		'''Value of variable $VEMT_PATH'''
		return self._instance.VemtPath

	@property
	def vemt_limit(self) -> int:
		'''Value of variable $VEMT_LIMIT'''
		return self._instance.VemtLimit

	@property
	def vircimg_siz(self) -> int:
		'''Value of variable $VIRCIMG_SIZ'''
		return self._instance.VircimgSiz

	@property
	def num_vr(self) -> int:
		'''Value of variable $NUM_VR'''
		return self._instance.NumVr

	@property
	def vrtd_delay(self) -> int:
		'''Value of variable $VRTD_DELAY'''
		return self._instance.VrtdDelay

	@property
	def max_nfound(self) -> int:
		'''Value of variable $MAX_NFOUND'''
		return self._instance.MaxNfound

	@property
	def diagbuf_siz(self) -> int:
		'''Value of variable $DIAGBUF_SIZ'''
		return self._instance.DiagbufSiz

	@property
	def rpos_xyz_th(self) -> float:
		'''Value of variable $RPOS_XYZ_TH'''
		return self._instance.RposXyzTh

	@property
	def rpos_wpr_th(self) -> float:
		'''Value of variable $RPOS_WPR_TH'''
		return self._instance.RposWprTh

	@property
	def rpos_ang_th(self) -> float:
		'''Value of variable $RPOS_ANG_TH'''
		return self._instance.RposAngTh

	@property
	def enb_virtcam(self) -> bool:
		'''Value of variable $ENB_VIRTCAM'''
		return self._instance.EnbVirtcam

	@property
	def imdiag_siz(self) -> int:
		'''Value of variable $IMDIAG_SIZ'''
		return self._instance.ImdiagSiz

	@property
	def vrtd_timout(self) -> int:
		'''Value of variable $VRTD_TIMOUT'''
		return self._instance.VrtdTimout

	@property
	def grabber_typ(self) -> int:
		'''Value of variable $GRABBER_TYP'''
		return self._instance.GrabberTyp

	@property
	def baslerusbca(self) -> int:
		'''Value of variable $BASLERUSBCA'''
		return self._instance.Baslerusbca

	@property
	def def_dsp_mod(self) -> int:
		'''Value of variable $DEF_DSP_MOD'''
		return self._instance.DefDspMod

	@property
	def dummy50(self) -> int:
		'''Value of variable $DUMMY50'''
		return self._instance.Dummy50

	@property
	def dummy51(self) -> int:
		'''Value of variable $DUMMY51'''
		return self._instance.Dummy51

	@property
	def dummy52(self) -> int:
		'''Value of variable $DUMMY52'''
		return self._instance.Dummy52

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VisionCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
