import typing
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.current_position_request import CurrentPositionRequest
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import CurrentPosition as current_position

class CurrentPosition(SnpxAssignableElements2[Position, CurrentPositionRequest]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position()
		else:
			self._instance = _internal
	def read_world_position(self, group: int) -> Position:
		return Position(None, None, None, None, self._instance.ReadWorldPosition(group))
	def read_user_frame_position(self, userFrame: int, group: int) -> Position:
		return Position(None, None, None, None, self._instance.ReadUserFramePosition(userFrame, group))
