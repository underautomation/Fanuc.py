import typing
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
from UnderAutomation.Fanuc.Rmi.Data import TcpSpeed as tcp_speed

class TcpSpeed(RmiTimedResponse):
	'''Result of reading TCP speed.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tcp_speed()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def speed(self) -> float:
		'''Current tool center point speed.'''
		return self._instance.Speed

	@speed.setter
	def speed(self, value: float):
		self._instance.Speed = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TcpSpeed):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
