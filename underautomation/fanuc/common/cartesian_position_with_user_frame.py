import typing
from underautomation.fanuc.common.cartesian_position_with_tool import CartesianPositionWithTool
from UnderAutomation.Fanuc.Common import CartesianPositionWithUserFrame as cartesian_position_with_user_frame

class CartesianPositionWithUserFrame(CartesianPositionWithTool):
	'''A cartesian tool position with a user frame ID'''
	def __init__(self, x: float, y: float, z: float, w: float, p: float, r: float, tool: int, frame: int, _internal = 0):
		'''Constructor with position, rotations, tool and frame IDs'''
		if(_internal == 0):
			self._instance = cartesian_position_with_user_frame(x, y, z, w, p, r, tool, frame)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def frame(self) -> int:
		'''Frame ID in the controller'''
		return self._instance.Frame

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPositionWithUserFrame):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
