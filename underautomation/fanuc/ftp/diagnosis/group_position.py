import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.common.cartesian_position_with_tool import CartesianPositionWithTool
from UnderAutomation.Fanuc.Ftp.Diagnosis import GroupPosition as group_position

class GroupPosition:
	'''Complete position information of a group'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = group_position()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def id(self) -> int:
		'''Group ID'''
		return self._instance.Id

	@property
	def joints_position(self) -> JointsPosition:
		'''Joint positions : the position of each robot angles'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.JointsPosition)

	@property
	def user_frame_positions(self) -> typing.List[CartesianPositionWithUserFrame]:
		'''Position of each tools in each user frames'''
		return [CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, x) for x in self._instance.UserFramePositions]

	@property
	def world_positions(self) -> typing.List[CartesianPositionWithTool]:
		'''Position of each tools in world coordinates'''
		return [CartesianPositionWithTool(None, None, None, None, None, None, None, x) for x in self._instance.WorldPositions]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GroupPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
