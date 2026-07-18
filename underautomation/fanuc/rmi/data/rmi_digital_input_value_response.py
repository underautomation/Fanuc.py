from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_on_off import RmiOnOff
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiDigitalInputValueResponse as rmi_digital_input_value_response
from UnderAutomation.Fanuc.Rmi.Data import RmiOnOff as rmi_on_off

class RmiDigitalInputValueResponse(RmiResponseBase):
	'''Result of reading a digital input.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_digital_input_value_response()
		else:
			self._instance = _internal

	@property
	def port_number(self) -> int:
		'''Port number.'''
		return self._instance.PortNumber

	@port_number.setter
	def port_number(self, value: int):
		self._instance.PortNumber = value

	@property
	def port_value(self) -> RmiOnOff:
		'''Port value'''
		return RmiOnOff(int(self._instance.PortValue))

	@port_value.setter
	def port_value(self, value: RmiOnOff):
		self._instance.PortValue = rmi_on_off(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiDigitalInputValueResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
