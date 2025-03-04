import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MfrqCfgVariableType as mfrq_cfg_variable_type

class MfrqCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mfrq_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def hrs_run(self) -> float:
		return self._instance.HrsRun
	@property
	def state(self) -> int:
		return self._instance.State
	@property
	def act_grp(self) -> int:
		return self._instance.ActGrp
	@property
	def freq_lim(self) -> float:
		return self._instance.FreqLim
	@property
	def win_size(self) -> int:
		return self._instance.WinSize
	@property
	def overlap(self) -> int:
		return self._instance.Overlap
	@property
	def flag(self) -> int:
		return self._instance.Flag
	@property
	def spd_ovrd(self) -> int:
		return self._instance.SpdOvrd
	@property
	def pg_prefix(self) -> str:
		return self._instance.PgPrefix
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
