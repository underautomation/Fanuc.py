import typing
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import TcpSpeed as tcp_speed

class TcpSpeed(RmiTimedResponse):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tcp_speed()
		else:
			self._instance = _internal
	@property
	def speed(self) -> float:
		return self._instance.Speed
	@speed.setter
	def speed(self, value: float):
		self._instance.Speed = value
