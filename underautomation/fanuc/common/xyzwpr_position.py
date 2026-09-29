from __future__ import annotations
import typing
from underautomation.fanuc.common.quaternion import Quaternion
from underautomation.fanuc.common.xyz_position import XYZPosition
from UnderAutomation.Fanuc.Common import XYZWPRPosition as xyzwpr_position

class XYZWPRPosition(XYZPosition):
	'''Cartesian position X, Y, Z with W, P, R rotations'''
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, _internal = 0):
		'''Constructor with position and rotations'''
		if(_internal == 0):
			self._instance = xyzwpr_position(x, y, z, w, p, r)
		else:
			self._instance = _internal

	def to_homogeneous_matrix(self) -> typing.List[float]:
		'''Convert position to a homogeneous rotation and translation 4x4 matrix'''
		return self._instance.ToHomogeneousMatrix()

	def get_quaternion(self) -> Quaternion:
		'''Returns the orientation W, P, R as a quaternion'''
		return Quaternion(None, None, None, None, self._instance.GetQuaternion())

	def set_quaternion(self, quaternion: Quaternion) -> None:
		'''Sets the orientation W, P, R from a quaternion. Angles are between -180 and 180 degrees.

		:param quaternion: Orientation
		'''
		self._instance.SetQuaternion(quaternion._instance if quaternion else None)

	def multiply(self, other: 'XYZWPRPosition') -> 'XYZWPRPosition':
		'''Returns the composition of this frame with another one: the pose other, expressed in this frame, converted to the frame where this position is expressed.

		:param other: Pose expressed in this frame
		'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.Multiply(other._instance if other else None))

	def inverse(self) -> 'XYZWPRPosition':
		'''Returns the inverse of this frame'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.Inverse())

	def flange_to_tcp(self, tool: 'XYZWPRPosition') -> 'XYZWPRPosition':
		'''Converts a flange position to the position of the tool center point (TCP)

		:param tool: Tool frame, relative to the flange (for example a UTOOL value)
		'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.FlangeToTcp(tool._instance if tool else None))

	def tcp_to_flange(self, tool: 'XYZWPRPosition') -> 'XYZWPRPosition':
		'''Converts a position of the tool center point (TCP) to the flange position

		:param tool: Tool frame, relative to the flange (for example a UTOOL value)
		'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.TcpToFlange(tool._instance if tool else None))

	def user_frame_to_world(self, userFrame: 'XYZWPRPosition') -> 'XYZWPRPosition':
		'''Converts this position, expressed in a user frame, to the world frame

		:param userFrame: User frame, relative to the world frame (for example a UFRAME value)
		'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.UserFrameToWorld(userFrame._instance if userFrame else None))

	def world_to_user_frame(self, userFrame: 'XYZWPRPosition') -> 'XYZWPRPosition':
		'''Converts this position, expressed in the world frame, to a user frame

		:param userFrame: User frame, relative to the world frame (for example a UFRAME value)
		'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.WorldToUserFrame(userFrame._instance if userFrame else None))

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

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XYZWPRPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
