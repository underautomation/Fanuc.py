import typing
from underautomation.fanuc.rmi.data.motion_configuration import MotionConfiguration
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
from UnderAutomation.Fanuc.Rmi.Data import CartesianPosition as cartesian_position

class CartesianPosition(RmiTimedResponse):
	'''Result of reading cartesian position.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def configuration(self) -> MotionConfiguration:
		'''Active configuration at sampling time.'''
		return MotionConfiguration(self._instance.Configuration)

	@configuration.setter
	def configuration(self, value: MotionConfiguration):
		self._instance.Configuration = value._instance if value else None

	@property
	def position(self) -> Frame:
		'''Cartesian TCP position.'''
		return Frame(self._instance.Position)

	@position.setter
	def position(self, value: Frame):
		self._instance.Position = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
