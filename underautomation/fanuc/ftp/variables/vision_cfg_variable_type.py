import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VisionCfgVariableType as vision_cfg_variable_type

class VisionCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vision_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def data_path(self) -> str:
		return self._instance.DataPath
	@property
	def data_cache(self) -> int:
		return self._instance.DataCache
	@property
	def log_path(self) -> str:
		return self._instance.LogPath
	@property
	def log_expath(self) -> str:
		return self._instance.LogExpath
	@property
	def log_timeout(self) -> int:
		return self._instance.LogTimeout
	@property
	def mc_limit(self) -> int:
		return self._instance.McLimit
	@property
	def fr_limit(self) -> int:
		return self._instance.FrLimit
	@property
	def td_limit(self) -> int:
		return self._instance.TdLimit
	@property
	def debug_mode(self) -> int:
		return self._instance.DebugMode
	@property
	def host_name(self) -> str:
		return self._instance.HostName
	@property
	def comm_port(self) -> int:
		return self._instance.CommPort
	@property
	def robot_name(self) -> str:
		return self._instance.RobotName
	@property
	def flags(self) -> int:
		return self._instance.Flags
	@property
	def flags2(self) -> int:
		return self._instance.Flags2
	@property
	def max_pages(self) -> int:
		return self._instance.MaxPages
	@property
	def min_vpool(self) -> int:
		return self._instance.MinVpool
	@property
	def vpool_size(self) -> int:
		return self._instance.VpoolSize
	@property
	def vpool_szcal(self) -> int:
		return self._instance.VpoolSzcal
	@property
	def vpool_lim(self) -> int:
		return self._instance.VpoolLim
	@property
	def vpool_wait(self) -> int:
		return self._instance.VpoolWait
	@property
	def tmppool_lim(self) -> int:
		return self._instance.TmppoolLim
	@property
	def failimg_idx(self) -> int:
		return self._instance.FailimgIdx
	@property
	def loadimg_idx(self) -> int:
		return self._instance.LoadimgIdx
	@property
	def num_imregs(self) -> int:
		return self._instance.NumImregs
	@property
	def imreg_size(self) -> int:
		return self._instance.ImregSize
	@property
	def gpm_candmax(self) -> int:
		return self._instance.GpmCandmax
	@property
	def num_asynbuf(self) -> int:
		return self._instance.NumAsynbuf
	@property
	def num_vrtdbuf(self) -> int:
		return self._instance.NumVrtdbuf
	@property
	def vrtdbuf_siz(self) -> int:
		return self._instance.VrtdbufSiz
	@property
	def tole2d_z(self) -> float:
		return self._instance.Tole2dZ
	@property
	def tole2d_wp(self) -> float:
		return self._instance.Tole2dWp
	@property
	def pc_setup(self) -> bool:
		return self._instance.PcSetup
	@property
	def logque_max(self) -> int:
		return self._instance.LogqueMax
	@property
	def eccu_retry(self) -> int:
		return self._instance.EccuRetry
	@property
	def vemt_path(self) -> str:
		return self._instance.VemtPath
	@property
	def vemt_limit(self) -> int:
		return self._instance.VemtLimit
	@property
	def vircimg_siz(self) -> int:
		return self._instance.VircimgSiz
	@property
	def num_vr(self) -> int:
		return self._instance.NumVr
	@property
	def vrtd_delay(self) -> int:
		return self._instance.VrtdDelay
	@property
	def max_nfound(self) -> int:
		return self._instance.MaxNfound
	@property
	def diagbuf_siz(self) -> int:
		return self._instance.DiagbufSiz
	@property
	def rpos_xyz_th(self) -> float:
		return self._instance.RposXyzTh
	@property
	def rpos_wpr_th(self) -> float:
		return self._instance.RposWprTh
	@property
	def rpos_ang_th(self) -> float:
		return self._instance.RposAngTh
	@property
	def enb_virtcam(self) -> bool:
		return self._instance.EnbVirtcam
	@property
	def imdiag_siz(self) -> int:
		return self._instance.ImdiagSiz
	@property
	def vrtd_timout(self) -> int:
		return self._instance.VrtdTimout
	@property
	def grabber_typ(self) -> int:
		return self._instance.GrabberTyp
	@property
	def baslerusbca(self) -> int:
		return self._instance.Baslerusbca
	@property
	def def_dsp_mod(self) -> int:
		return self._instance.DefDspMod
	@property
	def dummy50(self) -> int:
		return self._instance.Dummy50
	@property
	def dummy51(self) -> int:
		return self._instance.Dummy51
	@property
	def dummy52(self) -> int:
		return self._instance.Dummy52
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
