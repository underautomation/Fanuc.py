import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CartesianPositionVariable as cartesian_position_variable

class CartesianPositionVariable(CartesianPosition):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position_variable()
		else:
			self._instance = _internal
	@staticmethod
	def parse(value: str) -> 'CartesianPositionVariable':
		return CartesianPositionVariable(cartesian_position_variable.Parse(value))
	@property
	def group(self) -> int:
		return self._instance.Group
	@group.setter
	def group(self, value: int):
		self._instance.Group = value
