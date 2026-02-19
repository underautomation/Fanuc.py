import typing
from UnderAutomation.Fanuc.Common import XYZPosition as xyz_position

class XYZPosition:
	'''Cartesian position X, Y, Z'''
	def __init__(self, x: float, y: float, z: float, _internal = 0):
		'''Constructor with X, Y, Z coordinates in millimeters'''
		if(_internal == 0):
			self._instance = xyz_position(x, y, z)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def x(self) -> float:
		'''X coordinate in millimeters'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y coordinate in millimeters'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z coordinate in millimeters'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XYZPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
