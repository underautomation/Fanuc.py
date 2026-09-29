from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common import Quaternion as quaternion

class Quaternion:
	'''Quaternion that represents an orientation (Qw + Qx.i + Qy.j + Qz.k). Use get_quaternion() and set_quaternion() to convert from and to W, P, R angles.'''
	def __init__(self, qw: float, qx: float, qy: float, qz: float, _internal = 0):
		'''Creates a quaternion from its components

		:param qw: Scalar part
		:param qx: X component of the vector part
		:param qy: Y component of the vector part
		:param qz: Z component of the vector part
		'''
		if(_internal == 0):
			self._instance = quaternion(qw, qx, qy, qz)
		else:
			self._instance = _internal

	def normalize(self) -> 'Quaternion':
		'''Returns this quaternion with a norm of 1'''
		return Quaternion(None, None, None, None, self._instance.Normalize())

	def conjugate(self) -> 'Quaternion':
		'''Returns the conjugate of this quaternion. For a rotation, it is the inverse rotation.'''
		return Quaternion(None, None, None, None, self._instance.Conjugate())

	def multiply(self, other: 'Quaternion') -> 'Quaternion':
		'''Returns the product this x other: the rotation other applied after the rotation this, in the frame of this.

		:param other: Right operand
		'''
		return Quaternion(None, None, None, None, self._instance.Multiply(other._instance if other else None))

	def dot(self, other: 'Quaternion') -> float:
		'''Dot product of the two quaternions

		:param other: Other quaternion
		'''
		return self._instance.Dot(other._instance if other else None)

	def angle_to(self, other: 'Quaternion') -> float:
		'''Angle of the rotation between the two orientations, in degrees (0 to 180)

		:param other: Other orientation
		'''
		return self._instance.AngleTo(other._instance if other else None)

	@staticmethod
	def slerp(start: 'Quaternion', end: 'Quaternion', t: float) -> 'Quaternion':
		'''Spherical linear interpolation between two orientations, on the shortest way

		:param start: Orientation for t = 0
		:param end: Orientation for t = 1
		:param t: Interpolation parameter, usually between 0 and 1
		'''
		return Quaternion(None, None, None, None, quaternion.Slerp(start._instance if start else None, end._instance if end else None, t))

	@staticmethod
	def from_axis_angle(x: float, y: float, z: float, angle: float) -> 'Quaternion':
		'''Creates a rotation around an axis

		:param x: X component of the axis
		:param y: Y component of the axis
		:param z: Z component of the axis
		:param angle: Rotation angle in degrees
		'''
		return Quaternion(None, None, None, None, quaternion.FromAxisAngle(x, y, z, angle))

	def to_axis_angle(self) -> typing.List[float]:
		'''Returns the rotation axis and angle: [x, y, z, angle in degrees]. The axis is a unit vector and the angle is between 0 and 180.'''
		return self._instance.ToAxisAngle()

	@staticmethod
	def from_rotation_matrix(matrix: typing.List[float]) -> 'Quaternion':
		return Quaternion(None, None, None, None, quaternion.FromRotationMatrix(matrix))

	def to_rotation_matrix(self) -> typing.List[float]:
		'''Returns the 3x3 rotation matrix of this orientation'''
		return self._instance.ToRotationMatrix()

	@property
	def qw(self) -> float:
		'''Scalar part'''
		return self._instance.Qw

	@qw.setter
	def qw(self, value: float):
		self._instance.Qw = value

	@property
	def qx(self) -> float:
		'''X component of the vector part'''
		return self._instance.Qx

	@qx.setter
	def qx(self, value: float):
		self._instance.Qx = value

	@property
	def qy(self) -> float:
		'''Y component of the vector part'''
		return self._instance.Qy

	@qy.setter
	def qy(self, value: float):
		self._instance.Qy = value

	@property
	def qz(self) -> float:
		'''Z component of the vector part'''
		return self._instance.Qz

	@qz.setter
	def qz(self, value: float):
		self._instance.Qz = value

	@property
	def norm(self) -> float:
		'''Norm of the quaternion (1 for a rotation)'''
		return self._instance.Norm

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Quaternion):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
