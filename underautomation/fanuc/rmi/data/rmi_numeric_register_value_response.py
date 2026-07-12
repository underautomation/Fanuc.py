from __future__ import annotations
import typing
from underautomation.fanuc.common.numeric_register import NumericRegister
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiNumericRegisterValueResponse as rmi_numeric_register_value_response

class RmiNumericRegisterValueResponse(RmiResponseBase):
	'''Result of reading a numeric register.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_numeric_register_value_response()
		else:
			self._instance = _internal

	@property
	def register_number(self) -> int:
		'''Register number.'''
		return self._instance.RegisterNumber

	@register_number.setter
	def register_number(self, value: int):
		self._instance.RegisterNumber = value

	@property
	def value(self) -> NumericRegister:
		'''Register value.'''
		return NumericRegister(None, self._instance.Value)

	@value.setter
	def value(self, value: NumericRegister):
		self._instance.Value = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiNumericRegisterValueResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
