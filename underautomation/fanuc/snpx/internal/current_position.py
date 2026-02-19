import typing
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
from underautomation.fanuc.snpx.internal.current_position_request import CurrentPositionRequest
from UnderAutomation.Fanuc.Snpx.Internal import CurrentPosition as current_position

class CurrentPosition(SnpxAssignableElements2[Position, CurrentPositionRequest]):
	'''Provides access to the current robot position via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position()
		else:
			self._instance = _internal

	def read_world_position(self, group: int) -> Position:
		'''Reads the current world position of the specified motion group.

		:param group: The motion group number.
		:returns: The current position in world coordinates.
		'''
		return Position(None, None, None, None, self._instance.ReadWorldPosition(group))

	def read_user_frame_position(self, userFrame: int, group: int) -> Position:
		'''Reads the current position in the specified user frame and motion group.

		:param userFrame: The user frame number.
		:param group: The motion group number.
		:returns: The current position in the user frame.
		'''
		return Position(None, None, None, None, self._instance.ReadUserFramePosition(userFrame, group))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
