import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpT1ModeVariableType as cp_t1_mode_variable_type

class CpT1ModeVariableType(GenericVariableType):
	'''Describes the Fanuc type CP_T1_MODE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_t1_mode_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def comp_switch(self) -> int:
		'''Value of variable $COMP_SWITCH'''
		return self._instance.CompSwitch

	@property
	def margin(self) -> int:
		'''Value of variable $MARGIN'''
		return self._instance.Margin

	@property
	def time_factor(self) -> float:
		'''Value of variable $TIME_FACTOR'''
		return self._instance.TimeFactor

	@property
	def spd_limit(self) -> float:
		'''Value of variable $SPD_LIMIT'''
		return self._instance.SpdLimit

	@property
	def slew_rate(self) -> float:
		'''Value of variable $SLEW_RATE'''
		return self._instance.SlewRate

	@property
	def min_tflen(self) -> int:
		'''Value of variable $MIN_TFLEN'''
		return self._instance.MinTflen

	@property
	def extra_int(self) -> typing.List[int]:
		'''Value of variable $EXTRA_INT'''
		return self._instance.ExtraInt

	@property
	def extra_flt(self) -> typing.List[float]:
		'''Value of variable $EXTRA_FLT'''
		return self._instance.ExtraFlt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpT1ModeVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
