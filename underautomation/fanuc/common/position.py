import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from UnderAutomation.Fanuc.Common import Position as position

class Position:
	'''Robot position with joints and cartesian representations'''
	def __init__(self, userFrame: int, userTool: int, jointsPosition: JointsPosition, cartesianPosition: ExtendedCartesianPosition, _internal = 0):
		'''Constructor with user frame, tool, joints and cartesian position'''
		if(_internal == 0):
			self._instance = position(userFrame, userTool, jointsPosition, cartesianPosition)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def user_frame(self) -> int:
		'''User frame index'''
		return self._instance.UserFrame

	@user_frame.setter
	def user_frame(self, value: int):
		self._instance.UserFrame = value

	@property
	def user_tool(self) -> int:
		'''User tool index'''
		return self._instance.UserTool

	@user_tool.setter
	def user_tool(self, value: int):
		self._instance.UserTool = value

	@property
	def joints_position(self) -> JointsPosition:
		'''Joint values in degrees'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.JointsPosition)

	@joints_position.setter
	def joints_position(self, value: JointsPosition):
		self._instance.JointsPosition = value._instance if value else None

	@property
	def cartesian_position(self) -> ExtendedCartesianPosition:
		'''Cartesian position with extended axes'''
		return ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, self._instance.CartesianPosition)

	@cartesian_position.setter
	def cartesian_position(self, value: ExtendedCartesianPosition):
		self._instance.CartesianPosition = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Position):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
