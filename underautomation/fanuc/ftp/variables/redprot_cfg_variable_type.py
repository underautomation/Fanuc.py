import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RedprotCfgVariableType as redprot_cfg_variable_type

class RedprotCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = redprot_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def lvl2_pct(self) -> float:
		return self._instance.Lvl2Pct
	@property
	def lvl2_sev(self) -> int:
		return self._instance.Lvl2Sev
	@property
	def min_l10_cap(self) -> float:
		return self._instance.MinL10Cap
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
