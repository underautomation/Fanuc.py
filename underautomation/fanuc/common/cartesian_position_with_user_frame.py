import typing
from underautomation.fanuc.common.cartesian_position_with_tool import CartesianPositionWithTool
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import CartesianPositionWithUserFrame as cartesian_position_with_user_frame

class CartesianPositionWithUserFrame(CartesianPositionWithTool):
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, tool: int, frame: int, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position_with_user_frame(x, y, z, w, p, r, tool, frame)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def frame(self) -> int:
		return self._instance.Frame
