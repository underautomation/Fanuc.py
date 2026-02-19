import typing
from underautomation.fanuc.common.configuration import Configuration
from underautomation.fanuc.common.xyz_position import XYZPosition
from UnderAutomation.Fanuc.Common import CartesianPosition as cartesian_position

class CartesianPosition(XYZPosition):
	'''Fanuc cartesian position and rotations'''
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, configuration: Configuration, _internal = 0):
		'''Constructor with position, rotations and configuration'''
		if(_internal == 0):
			self._instance = cartesian_position(x, y, z, w, p, r, configuration)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def to_homogeneous_matrix(self) -> typing.List[float]:
		'''Convert position to a homogeneous rotation and translation 4x4 matrix'''
		return self._instance.ToHomogeneousMatrix()

	@staticmethod
	def from_homogeneous_matrix(R: typing.List[float]) -> 'CartesianPosition':
		return CartesianPosition(None, None, None, None, None, None, None, cartesian_position.FromHomogeneousMatrix(R))

	@staticmethod
	def normalize_angle(angle: float) -> float:
		'''Normalize an angle to the range ]-180, 180]'''
		return cartesian_position.NormalizeAngle(angle)

	@staticmethod
	def normalize_angles(pose: 'CartesianPosition') -> None:
		'''Normalize the W, P, R angles to the range ]-180, 180]'''
		cartesian_position.NormalizeAngles(pose._instance if pose else None)

	@staticmethod
	def is_near(a: 'CartesianPosition', b: 'CartesianPosition', mmTolerance: float, degreesTolerance: float) -> bool:
		'''Check if two Cartesian positions are near each other within specified tolerances'''
		return cartesian_position.IsNear(a._instance if a else None, b._instance if b else None, mmTolerance, degreesTolerance)

	@property
	def w(self) -> float:
		'''W rotation in degrees (Rx)'''
		return self._instance.W

	@w.setter
	def w(self, value: float):
		self._instance.W = value

	@property
	def p(self) -> float:
		'''P rotation in degrees (Ry)'''
		return self._instance.P

	@p.setter
	def p(self, value: float):
		self._instance.P = value

	@property
	def r(self) -> float:
		'''R rotation in degrees (Rz)'''
		return self._instance.R

	@r.setter
	def r(self, value: float):
		self._instance.R = value

	@property
	def configuration(self) -> Configuration:
		'''Position configuration'''
		return Configuration(None, None, None, None, None, None, None, self._instance.Configuration)

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
