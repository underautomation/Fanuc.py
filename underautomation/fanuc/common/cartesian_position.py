import typing
from underautomation.fanuc.common.configuration import Configuration
from underautomation.fanuc.common.xyz_position import XYZPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import CartesianPosition as cartesian_position

class CartesianPosition(XYZPosition):
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, configuration: Configuration, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position(x, y, z, w, p, r, configuration)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	def to_homogeneous_matrix(self) -> typing.List[float]:
		return self._instance.ToHomogeneousMatrix()
	@staticmethod
	def from_homogeneous_matrix(R: typing.List[float]) -> 'CartesianPosition':
		return CartesianPosition(None, None, None, None, None, None, None, cartesian_position.FromHomogeneousMatrix(R))
	@staticmethod
	def normalize_angle(angle: float) -> float:
		return cartesian_position.NormalizeAngle(angle)
	@staticmethod
	def normalize_angles(pose: 'CartesianPosition') -> None:
		cartesian_position.NormalizeAngles(pose._instance if pose else None)
	@staticmethod
	def is_near(a: 'CartesianPosition', b: 'CartesianPosition', mmTolerance: float, degreesTolerance: float) -> bool:
		return cartesian_position.IsNear(a._instance if a else None, b._instance if b else None, mmTolerance, degreesTolerance)
	@property
	def w(self) -> float:
		return self._instance.W
	@w.setter
	def w(self, value: float):
		self._instance.W = value
	@property
	def p(self) -> float:
		return self._instance.P
	@p.setter
	def p(self, value: float):
		self._instance.P = value
	@property
	def r(self) -> float:
		return self._instance.R
	@r.setter
	def r(self, value: float):
		self._instance.R = value
	@property
	def configuration(self) -> Configuration:
		return Configuration(None, None, None, None, None, None, None, self._instance.Configuration)
