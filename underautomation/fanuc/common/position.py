import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import Position as position

class Position:
	def __init__(self, userFrame: int, userTool: int, jointsPosition: JointsPosition, cartesianPosition: ExtendedCartesianPosition, _internal = 0):
		if(_internal == 0):
			self._instance = position(userFrame, userTool, jointsPosition, cartesianPosition)
		else:
			self._instance = _internal
	@property
	def user_frame(self) -> int:
		return self._instance.UserFrame
	@user_frame.setter
	def user_frame(self, value: int):
		self._instance.UserFrame = value
	@property
	def user_tool(self) -> int:
		return self._instance.UserTool
	@user_tool.setter
	def user_tool(self, value: int):
		self._instance.UserTool = value
	@property
	def joints_position(self) -> JointsPosition:
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.JointsPosition)
	@joints_position.setter
	def joints_position(self, value: JointsPosition):
		self._instance.JointsPosition = value
	@property
	def cartesian_position(self) -> ExtendedCartesianPosition:
		return ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, self._instance.CartesianPosition)
	@cartesian_position.setter
	def cartesian_position(self, value: ExtendedCartesianPosition):
		self._instance.CartesianPosition = value
