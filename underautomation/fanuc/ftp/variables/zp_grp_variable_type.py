import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZpGrpVariableType as zp_grp_variable_type

class ZpGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zp_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def options(self) -> typing.List[int]:
		return self._instance.Options
	@property
	def break_time(self) -> int:
		return self._instance.BreakTime
	@property
	def work_shift(self) -> int:
		return self._instance.WorkShift
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def rv_life(self) -> typing.List[int]:
		return self._instance.RvLife
	@property
	def shift_ovc(self) -> typing.List[float]:
		return self._instance.ShiftOvc
	@property
	def part_id(self) -> int:
		return self._instance.PartId
	@property
	def optm_rate(self) -> typing.List[float]:
		return self._instance.OptmRate
	@property
	def max_i_rate(self) -> int:
		return self._instance.MaxIRate
	@property
	def max_di_rate(self) -> int:
		return self._instance.MaxDiRate
	@property
	def trace_env(self) -> float:
		return self._instance.TraceEnv
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
