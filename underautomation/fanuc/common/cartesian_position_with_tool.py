import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from UnderAutomation.Fanuc.Common import CartesianPositionWithTool as cartesian_position_with_tool

class CartesianPositionWithTool(CartesianPosition):
	'''A cartesian position with a tool ID'''
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, tool: int, _internal = 0):
		'''Constructor with position, rotations and tool ID'''
		if(_internal == 0):
			self._instance = cartesian_position_with_tool(x, y, z, w, p, r, tool)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def tool(self) -> int:
		'''Tool ID'''
		return self._instance.Tool

	@tool.setter
	def tool(self, value: int):
		self._instance.Tool = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPositionWithTool):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
