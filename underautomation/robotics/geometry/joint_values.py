from __future__ import annotations
import typing
from UnderAutomation.Robotics.Geometry import JointValues as joint_values

class JointValues:
	'''Position of the axes of a robot: one value per axis, in degrees for rotary axes and in mm for linear axes'''
	def __init__(self, values: typing.List[float], _internal = 0):
		'''Creates a joint position from the values of the axes. The array is copied.

		:param values: Value of each axis
		'''
		if(_internal == 0):
			self._instance = joint_values(values)
		else:
			self._instance = _internal

	@property
	def values(self) -> typing.List[float]:
		'''Value of each axis, in degrees or mm'''
		return self._instance.Values

	@property
	def count(self) -> int:
		'''Number of axes'''
		return self._instance.Count

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointValues):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
