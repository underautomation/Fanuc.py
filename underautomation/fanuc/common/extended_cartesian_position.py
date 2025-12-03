import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ExtendedCartesianPosition as extended_cartesian_position

class ExtendedCartesianPosition(CartesianPosition):
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, e1: float, e2: float, e3: float, _internal = 0):
		if(_internal == 0):
			self._instance = extended_cartesian_position(x, y, z, w, p, r, e1, e2, e3)
		else:
			self._instance = _internal
	@property
	def e1(self) -> float:
		return self._instance.E1
	@e1.setter
	def e1(self, value: float):
		self._instance.E1 = value
	@property
	def e2(self) -> float:
		return self._instance.E2
	@e2.setter
	def e2(self, value: float):
		self._instance.E2 = value
	@property
	def e3(self) -> float:
		return self._instance.E3
	@e3.setter
	def e3(self, value: float):
		self._instance.E3 = value
