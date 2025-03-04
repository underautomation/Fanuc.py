import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import XYZPosition as xyz_position

class XYZPosition:
	def __init__(self, x: float, y: float, z: float, _internal = 0):
		if(_internal == 0):
			self._instance = xyz_position(x, y, z)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def x(self) -> float:
		return self._instance.X
	@x.setter
	def x(self, value: float):
		self._instance.X = value
	@property
	def y(self) -> float:
		return self._instance.Y
	@y.setter
	def y(self, value: float):
		self._instance.Y = value
	@property
	def z(self) -> float:
		return self._instance.Z
	@z.setter
	def z(self, value: float):
		self._instance.Z = value
