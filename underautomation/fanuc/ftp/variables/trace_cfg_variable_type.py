import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TraceCfgVariableType as trace_cfg_variable_type

class TraceCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type TRACE_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trace_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def items(self) -> int:
		'''Value of variable $ITEMS'''
		return self._instance.Items

	@property
	def channels(self) -> int:
		'''Value of variable $CHANNELS'''
		return self._instance.Channels

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def ticks(self) -> int:
		'''Value of variable $TICKS'''
		return self._instance.Ticks

	@property
	def min_mm(self) -> float:
		'''Value of variable $MIN_MM'''
		return self._instance.MinMm

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TraceCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
