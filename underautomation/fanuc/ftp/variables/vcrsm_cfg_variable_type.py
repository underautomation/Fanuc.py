import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcrsmCfgVariableType as vcrsm_cfg_variable_type

class VcrsmCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcrsm_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def step_num(self) -> int:
		return self._instance.StepNum
	@property
	def is_started(self) -> bool:
		return self._instance.IsStarted
	@property
	def cur_prog(self) -> str:
		return self._instance.CurProg
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
