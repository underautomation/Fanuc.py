import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import DigitalInputValue as digital_input_value

class DigitalInputValue(RmiResponseBase):
	'''Result of reading a digital input.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = digital_input_value()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def port_number(self) -> int:
		'''Port number.'''
		return self._instance.PortNumber

	@port_number.setter
	def port_number(self, value: int):
		self._instance.PortNumber = value

	@property
	def port_value(self) -> int:
		'''Port value (0 = OFF, 1 = ON).'''
		return self._instance.PortValue

	@port_value.setter
	def port_value(self, value: int):
		self._instance.PortValue = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DigitalInputValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
