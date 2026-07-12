from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiVariableValueResponse as rmi_variable_value_response

class RmiVariableValueResponse(RmiResponseBase):
	'''Result of reading a system variable.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_variable_value_response()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Variable name, including the leading $ character.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def is_integer(self) -> bool:
		'''Whether the variable holds a floating-point value.'''
		return self._instance.IsInteger

	@is_integer.setter
	def is_integer(self, value: bool):
		self._instance.IsInteger = value

	@property
	def integer_value(self) -> int:
		'''Gets or sets the value as an integer. Internally stored as a double.'''
		return self._instance.IntegerValue

	@integer_value.setter
	def integer_value(self, value: int):
		self._instance.IntegerValue = value

	@property
	def real_value(self) -> float:
		'''Gets or sets the value as a double-precision floating-point number.'''
		return self._instance.RealValue

	@real_value.setter
	def real_value(self, value: float):
		self._instance.RealValue = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiVariableValueResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
