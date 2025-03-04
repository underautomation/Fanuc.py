import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpT1ModeVariableType as cp_t1_mode_variable_type

class CpT1ModeVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_t1_mode_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def comp_switch(self) -> int:
		return self._instance.CompSwitch
	@property
	def margin(self) -> int:
		return self._instance.Margin
	@property
	def time_factor(self) -> float:
		return self._instance.TimeFactor
	@property
	def spd_limit(self) -> float:
		return self._instance.SpdLimit
	@property
	def slew_rate(self) -> float:
		return self._instance.SlewRate
	@property
	def min_tflen(self) -> int:
		return self._instance.MinTflen
	@property
	def extra_int(self) -> typing.List[int]:
		return self._instance.ExtraInt
	@property
	def extra_flt(self) -> typing.List[float]:
		return self._instance.ExtraFlt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
