import typing
from underautomation.fanuc.ftp.variables.eff_axis_variable_type import EffAxisVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AdjRtrqVariableType as adj_rtrq_variable_type

class AdjRtrqVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = adj_rtrq_variable_type()
		else:
			self._instance = _internal
	@property
	def cor_trq(self) -> typing.List[float]:
		return self._instance.CorTrq
	@property
	def cor_temp(self) -> typing.List[float]:
		return self._instance.CorTemp
	@property
	def eff_axis(self) -> typing.List[EffAxisVariableType]:
		return [EffAxisVariableType(x) for x in self._instance.EffAxis]
	@property
	def limit(self) -> float:
		return self._instance.Limit
	@property
	def adj_num(self) -> int:
		return self._instance.AdjNum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
