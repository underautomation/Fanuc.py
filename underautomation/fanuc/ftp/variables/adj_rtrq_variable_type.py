import typing
from underautomation.fanuc.ftp.variables.eff_axis_variable_type import EffAxisVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AdjRtrqVariableType as adj_rtrq_variable_type

class AdjRtrqVariableType(GenericVariableType):
	'''Describes the Fanuc type ADJ_RTRQ_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = adj_rtrq_variable_type()
		else:
			self._instance = _internal

	@property
	def cor_trq(self) -> typing.List[float]:
		'''Value of variable $COR_TRQ'''
		return self._instance.CorTrq

	@property
	def cor_temp(self) -> typing.List[float]:
		'''Value of variable $COR_TEMP'''
		return self._instance.CorTemp

	@property
	def eff_axis(self) -> typing.List[EffAxisVariableType]:
		'''Value of variable $EFF_AXIS'''
		return [EffAxisVariableType(x) for x in self._instance.EffAxis]

	@property
	def limit(self) -> float:
		'''Value of variable $LIMIT'''
		return self._instance.Limit

	@property
	def adj_num(self) -> int:
		'''Value of variable $ADJ_NUM'''
		return self._instance.AdjNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AdjRtrqVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
