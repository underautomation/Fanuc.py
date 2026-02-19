import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FltrOvrnVariableType as fltr_ovrn_variable_type

class FltrOvrnVariableType(GenericVariableType):
	'''Describes the Fanuc type $FLTR_OVRN'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fltr_ovrn_variable_type()
		else:
			self._instance = _internal

	@property
	def limit_tick(self) -> int:
		'''Value of variable $LIMIT_TICK'''
		return self._instance.LimitTick

	@property
	def overrun_cnt(self) -> int:
		'''Value of variable $OVERRUN_CNT'''
		return self._instance.OverrunCnt

	@property
	def max_tick(self) -> int:
		'''Value of variable $MAX_TICK'''
		return self._instance.MaxTick

	@property
	def itp_count(self) -> int:
		'''Value of variable $ITP_COUNT'''
		return self._instance.ItpCount

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FltrOvrnVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
