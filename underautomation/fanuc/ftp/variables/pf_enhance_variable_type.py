import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PfEnhanceVariableType as pf_enhance_variable_type

class PfEnhanceVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_enhance_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def state(self) -> int:
		return self._instance.State
	@property
	def hrs_intv(self) -> float:
		return self._instance.HrsIntv
	@property
	def rm_cfg(self) -> int:
		return self._instance.RmCfg
	@property
	def grp_mask(self) -> int:
		return self._instance.GrpMask
	@property
	def spd_ovrd(self) -> int:
		return self._instance.SpdOvrd
	@property
	def pg_prefix(self) -> str:
		return self._instance.PgPrefix
	@property
	def max_lines(self) -> int:
		return self._instance.MaxLines
	@property
	def ovc_lim(self) -> int:
		return self._instance.OvcLim
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
