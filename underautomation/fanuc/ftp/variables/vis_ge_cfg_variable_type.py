import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VisGeCfgVariableType as vis_ge_cfg_variable_type

class VisGeCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type VIS_GE_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vis_ge_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def max_img_sz(self) -> int:
		'''Value of variable $MAX_IMG_SZ'''
		return self._instance.MaxImgSz

	@property
	def max_img_tm(self) -> int:
		'''Value of variable $MAX_IMG_TM'''
		return self._instance.MaxImgTm

	@property
	def max_cam_res(self) -> int:
		'''Value of variable $MAX_CAM_RES'''
		return self._instance.MaxCamRes

	@property
	def num_retries(self) -> int:
		'''Value of variable $NUM_RETRIES'''
		return self._instance.NumRetries

	@property
	def retry_delay(self) -> int:
		'''Value of variable $RETRY_DELAY'''
		return self._instance.RetryDelay

	@property
	def dbg_level(self) -> int:
		'''Value of variable $DBG_LEVEL'''
		return self._instance.DbgLevel

	@property
	def spkt_delay(self) -> int:
		'''Value of variable $SPKT_DELAY'''
		return self._instance.SpktDelay

	@property
	def cfg_flags(self) -> int:
		'''Value of variable $CFG_FLAGS'''
		return self._instance.CfgFlags

	@property
	def gige_norese(self) -> bool:
		'''Value of variable $GIGE_NORESE'''
		return self._instance.GigeNorese

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VisGeCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
