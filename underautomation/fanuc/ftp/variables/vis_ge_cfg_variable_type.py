import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VisGeCfgVariableType as vis_ge_cfg_variable_type

class VisGeCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vis_ge_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def max_img_sz(self) -> int:
		return self._instance.MaxImgSz
	@property
	def max_img_tm(self) -> int:
		return self._instance.MaxImgTm
	@property
	def max_cam_res(self) -> int:
		return self._instance.MaxCamRes
	@property
	def num_retries(self) -> int:
		return self._instance.NumRetries
	@property
	def retry_delay(self) -> int:
		return self._instance.RetryDelay
	@property
	def dbg_level(self) -> int:
		return self._instance.DbgLevel
	@property
	def spkt_delay(self) -> int:
		return self._instance.SpktDelay
	@property
	def cfg_flags(self) -> int:
		return self._instance.CfgFlags
	@property
	def gige_norese(self) -> bool:
		return self._instance.GigeNorese
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
