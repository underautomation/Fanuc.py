import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ZpGrpVariableType as zp_grp_variable_type

class ZpGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type ZP_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zp_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def options(self) -> typing.List[int]:
		'''Value of variable $OPTIONS'''
		return self._instance.Options

	@property
	def break_time(self) -> int:
		'''Value of variable $BREAK_TIME'''
		return self._instance.BreakTime

	@property
	def work_shift(self) -> int:
		'''Value of variable $WORK_SHIFT'''
		return self._instance.WorkShift

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def rv_life(self) -> typing.List[int]:
		'''Value of variable $RV_LIFE'''
		return self._instance.RvLife

	@property
	def shift_ovc(self) -> typing.List[float]:
		'''Value of variable $SHIFT_OVC'''
		return self._instance.ShiftOvc

	@property
	def part_id(self) -> int:
		'''Value of variable $PART_ID'''
		return self._instance.PartId

	@property
	def optm_rate(self) -> typing.List[float]:
		'''Value of variable $OPTM_RATE'''
		return self._instance.OptmRate

	@property
	def max_i_rate(self) -> int:
		'''Value of variable $MAX_I_RATE'''
		return self._instance.MaxIRate

	@property
	def max_di_rate(self) -> int:
		'''Value of variable $MAX_DI_RATE'''
		return self._instance.MaxDiRate

	@property
	def trace_env(self) -> float:
		'''Value of variable $TRACE_ENV'''
		return self._instance.TraceEnv

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ZpGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
