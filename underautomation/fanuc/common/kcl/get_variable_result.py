from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.generic_variable import GenericVariable
from underautomation.fanuc.common.kcl.result import Result
from UnderAutomation.Fanuc.Common.Kcl import GetVariableResult as get_variable_result

class GetVariableResult(Result):
	'''Result of a get variable command containing the raw value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_variable_result()
		else:
			self._instance = _internal

	def parse_result(self) -> GenericVariable:
		'''Returns a structured object which represents the variable (not supported with Telnet)'''
		return GenericVariable(self._instance.ParseResult())

	@property
	def raw_value(self) -> str:
		'''Gets the raw value of the variable as a string.'''
		return self._instance.RawValue

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetVariableResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
