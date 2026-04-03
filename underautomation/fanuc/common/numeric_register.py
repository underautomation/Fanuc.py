from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common import NumericRegister as numeric_register

class NumericRegister:
	'''Represents a numeric register value that can be either integer or real.'''
	def __init__(self, value: int, _internal = 0):
		'''Creates a numeric register with an integer value.'''
		if(_internal == 0):
			self._instance = numeric_register(value)
		else:
			self._instance = _internal

	@property
	def is_integer(self) -> bool:
		'''Indicates whether the register holds an integer value (true) or a real value (false)'''
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
		if not isinstance(other, NumericRegister):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
