import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import DigitalInputValue as digital_input_value

class DigitalInputValue(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = digital_input_value()
		else:
			self._instance = _internal
	@property
	def port_number(self) -> int:
		return self._instance.PortNumber
	@port_number.setter
	def port_number(self, value: int):
		self._instance.PortNumber = value
	@property
	def port_value(self) -> int:
		return self._instance.PortValue
	@port_value.setter
	def port_value(self, value: int):
		self._instance.PortValue = value
