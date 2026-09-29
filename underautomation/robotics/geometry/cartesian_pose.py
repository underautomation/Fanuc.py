from __future__ import annotations
import typing
from underautomation.robotics.geometry.orientation import Orientation
from underautomation.robotics.geometry.euler_convention import EulerConvention
from UnderAutomation.Robotics.Geometry import CartesianPose as cartesian_pose
from UnderAutomation.Robotics.Geometry import EulerConvention as euler_convention

class CartesianPose:
	'''Cartesian pose: position X, Y, Z in mm, orientation, and optional values of external axes (mm or degrees). It can describe a position of the robot or a frame.'''
	def __init__(self, x: float, y: float, z: float, orientation: Orientation, _internal = 0):
		'''Creates a pose from a position and an orientation, without external axes

		:param x: X in mm
		:param y: Y in mm
		:param z: Z in mm
		:param orientation: Orientation (null for no rotation)
		'''
		if(_internal == 0):
			self._instance = cartesian_pose(x, y, z, orientation._instance if orientation else None)
		else:
			self._instance = _internal

	@staticmethod
	def from_euler(x: float, y: float, z: float, a: float, b: float, c: float, convention: EulerConvention) -> 'CartesianPose':
		'''Creates a pose from a position and three Euler angles, without external axes

		:param x: X in mm
		:param y: Y in mm
		:param z: Z in mm
		:param a: First angle in degrees
		:param b: Second angle in degrees
		:param c: Third angle in degrees
		:param convention: Convention of the angles
		'''
		return CartesianPose(None, None, None, None, cartesian_pose.FromEuler(x, y, z, a, b, c, euler_convention(int(convention))))

	def multiply(self, other: 'CartesianPose') -> 'CartesianPose':
		'''Returns the composition of this frame with another pose: the pose other, expressed in this frame, converted to the frame where this pose is expressed. The external axes of the result are the ones of other.

		:param other: Pose expressed in this frame
		'''
		return CartesianPose(None, None, None, None, self._instance.Multiply(other._instance if other else None))

	def inverse(self) -> 'CartesianPose':
		'''Returns the inverse of this frame. The result has no external axes.'''
		return CartesianPose(None, None, None, None, self._instance.Inverse())

	@property
	def x(self) -> float:
		'''X in mm'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y in mm'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z in mm'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def orientation(self) -> Orientation:
		'''Orientation. Setting null gives the identity orientation.'''
		return Orientation(self._instance.Orientation)

	@orientation.setter
	def orientation(self, value: Orientation):
		self._instance.Orientation = value._instance if value else None

	@property
	def external_axes(self) -> typing.List[float]:
		'''Values of the external axes, in mm or degrees. Empty when the pose has no external axes. Setting null gives an empty array.'''
		return self._instance.ExternalAxes

	@external_axes.setter
	def external_axes(self, value: typing.List[float]):
		self._instance.ExternalAxes = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPose):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
