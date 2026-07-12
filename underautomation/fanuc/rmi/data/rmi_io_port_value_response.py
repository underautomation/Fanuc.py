from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_io_port_type import RmiIoPortType
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiIoPortValueResponse as rmi_io_port_value_response
from UnderAutomation.Fanuc.Rmi.Data import RmiIoPortType as rmi_io_port_type

class RmiIoPortValueResponse(RmiResponseBase):
	'''Result of reading a generic IO port.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_io_port_value_response()
		else:
			self._instance = _internal

	@property
	def port_type(self) -> RmiIoPortType:
		'''Port type (DI, DO, AI, AO, GO, etc.).'''
		return RmiIoPortType(int(self._instance.PortType))

	@port_type.setter
	def port_type(self, value: RmiIoPortType):
		self._instance.PortType = rmi_io_port_type(int(value))

	@property
	def port_number(self) -> int:
		'''Port number.'''
		return self._instance.PortNumber

	@port_number.setter
	def port_number(self, value: int):
		self._instance.PortNumber = value

	@property
	def value(self) -> float:
		'''Current port value.'''
		return self._instance.Value

	@value.setter
	def value(self, value: float):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiIoPortValueResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
