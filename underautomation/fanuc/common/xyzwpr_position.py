from __future__ import annotations
import typing
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

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

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
