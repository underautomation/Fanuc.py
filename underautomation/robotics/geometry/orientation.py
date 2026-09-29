from __future__ import annotations
import typing
from underautomation.robotics.geometry.euler_convention import EulerConvention
from UnderAutomation.Robotics.Geometry import Orientation as orientation
from UnderAutomation.Robotics.Geometry import EulerConvention as euler_convention

class Orientation:
	'''Orientation in space, stored as a unit quaternion (Qw + Qx.i + Qy.j + Qz.k). It can be created from and converted to Euler angles, a rotation vector, an axis and an angle, or a rotation matrix.'''
	def __init__(self, _internal = 0):
		'''Creates the identity orientation (no rotation)'''
		if(_internal == 0):
			self._instance = orientation()
		else:
			self._instance = _internal

	@staticmethod
	def from_quaternion(qw: float, qx: float, qy: float, qz: float) -> 'Orientation':
		'''Creates an orientation from a quaternion. The quaternion is normalized.

		:param qw: Scalar part
		:param qx: X component of the vector part
		:param qy: Y component of the vector part
		:param qz: Z component of the vector part
		'''
		return Orientation(orientation.FromQuaternion(qw, qx, qy, qz))

	@staticmethod
	def from_euler(a: float, b: float, c: float, convention: EulerConvention) -> 'Orientation':
		'''Creates an orientation from three Euler angles

		:param a: First angle in degrees
		:param b: Second angle in degrees
		:param c: Third angle in degrees
		:param convention: Convention of the angles
		'''
		return Orientation(orientation.FromEuler(a, b, c, euler_convention(int(convention))))

	def to_euler(self, convention: EulerConvention) -> typing.List[float]:
		'''Returns the three Euler angles [a, b, c] of this orientation, in degrees. For MobileZYZ, b is between 0 and 180. For the other conventions, b is between -90 and 90. When the orientation is singular (b = 0 or 180 for ZYZ, b = -90 or 90 for the others), only a combination of a and c is defined: a is set to 0 for FixedXYZ, and c is set to 0 for the other conventions.

		:param convention: Convention of the angles
		'''
		return self._instance.ToEuler(euler_convention(int(convention)))

	@staticmethod
	def from_axis_angle(x: float, y: float, z: float, angle: float) -> 'Orientation':
		'''Creates a rotation around an axis

		:param x: X component of the axis
		:param y: Y component of the axis
		:param z: Z component of the axis
		:param angle: Rotation angle in degrees
		'''
		return Orientation(orientation.FromAxisAngle(x, y, z, angle))

	def to_axis_angle(self) -> typing.List[float]:
		'''Returns the rotation axis and angle: [x, y, z, angle in degrees]. The axis is a unit vector and the angle is between 0 and 180.'''
		return self._instance.ToAxisAngle()

	@staticmethod
	def from_rotation_vector(x: float, y: float, z: float) -> 'Orientation':
		'''Creates an orientation from a rotation vector: its direction is the rotation axis and its norm is the angle in degrees

		:param x: X component
		:param y: Y component
		:param z: Z component
		'''
		return Orientation(orientation.FromRotationVector(x, y, z))

	def to_rotation_vector(self) -> typing.List[float]:
		'''Returns the rotation vector [x, y, z] of this orientation: its direction is the rotation axis and its norm is the angle in degrees (0 to 180)'''
		return self._instance.ToRotationVector()

	@staticmethod
	def from_rotation_matrix(matrix: typing.List[float]) -> 'Orientation':
		return Orientation(orientation.FromRotationMatrix(matrix))

	def to_rotation_matrix(self) -> typing.List[float]:
		'''Returns the 3x3 rotation matrix of this orientation'''
		return self._instance.ToRotationMatrix()

	def multiply(self, other: 'Orientation') -> 'Orientation':
		'''Returns the composition this x other: the orientation other, expressed in the frame of this orientation, converted to the reference frame

		:param other: Right operand
		'''
		return Orientation(self._instance.Multiply(other._instance if other else None))

	def inverse(self) -> 'Orientation':
		'''Returns the inverse rotation'''
		return Orientation(self._instance.Inverse())

	def angle_to(self, other: 'Orientation') -> float:
		'''Angle of the rotation between the two orientations, in degrees (0 to 180)

		:param other: Other orientation
		'''
		return self._instance.AngleTo(other._instance if other else None)

	@staticmethod
	def slerp(start: 'Orientation', end: 'Orientation', t: float) -> 'Orientation':
		'''Spherical linear interpolation between two orientations, on the shortest way

		:param start: Orientation for t = 0
		:param end: Orientation for t = 1
		:param t: Interpolation parameter, usually between 0 and 1
		'''
		return Orientation(orientation.Slerp(start._instance if start else None, end._instance if end else None, t))

	@property
	def qw(self) -> float:
		'''Scalar part of the unit quaternion'''
		return self._instance.Qw

	@property
	def qx(self) -> float:
		'''X component of the vector part of the unit quaternion'''
		return self._instance.Qx

	@property
	def qy(self) -> float:
		'''Y component of the vector part of the unit quaternion'''
		return self._instance.Qy

	@property
	def qz(self) -> float:
		'''Z component of the vector part of the unit quaternion'''
		return self._instance.Qz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Orientation):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
