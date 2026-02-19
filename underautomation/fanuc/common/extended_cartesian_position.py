import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from UnderAutomation.Fanuc.Common import ExtendedCartesianPosition as extended_cartesian_position

class ExtendedCartesianPosition(CartesianPosition):
	'''Cartesian position with extended axes (E1, E2, E3)'''
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, e1: float, e2: float, e3: float, _internal = 0):
		'''Constructor with position, rotations, and extended axes'''
		if(_internal == 0):
			self._instance = extended_cartesian_position(x, y, z, w, p, r, e1, e2, e3)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def e1(self) -> float:
		'''Extended axis 1 value'''
		return self._instance.E1

	@e1.setter
	def e1(self, value: float):
		self._instance.E1 = value

	@property
	def e2(self) -> float:
		'''Extended axis 2 value'''
		return self._instance.E2

	@e2.setter
	def e2(self, value: float):
		self._instance.E2 = value

	@property
	def e3(self) -> float:
		'''Extended axis 3 value'''
		return self._instance.E3

	@e3.setter
	def e3(self, value: float):
		self._instance.E3 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ExtendedCartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
