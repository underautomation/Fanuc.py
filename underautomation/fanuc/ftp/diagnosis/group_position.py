import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.common.cartesian_position_with_tool import CartesianPositionWithTool
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import GroupPosition as group_position

class GroupPosition:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = group_position()
		else:
			self._instance = _internal
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def joints_position(self) -> JointsPosition:
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.JointsPosition)
	@property
	def user_frame_positions(self) -> typing.List[CartesianPositionWithUserFrame]:
		return [CartesianPositionWithUserFrame(x) for x in self._instance.UserFramePositions]
	@property
	def world_positions(self) -> typing.List[CartesianPositionWithTool]:
		return [CartesianPositionWithTool(x) for x in self._instance.WorldPositions]
