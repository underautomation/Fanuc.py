import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import CartesianPositionWithTool as cartesian_position_with_tool

class CartesianPositionWithTool(CartesianPosition):
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, tool: int, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position_with_tool(x, y, z, w, p, r, tool)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def tool(self) -> int:
		return self._instance.Tool
	@tool.setter
	def tool(self, value: int):
		self._instance.Tool = value
