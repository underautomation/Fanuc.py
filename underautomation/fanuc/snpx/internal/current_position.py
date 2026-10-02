from __future__ import annotations
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

	def read(self, index: CurrentPositionRequest) -> Position:
		return Position(None, None, None, None, self._instance.Read(index._instance if index else None))

	@typing.overload
	def read_world_position(self, group: int) -> Position: ...

	@typing.overload
	def read_world_position(self) -> Position: ...

	def read_world_position(self, *args, **kwargs) -> Position:
		'''Reads the current world position of the specified motion group.
		Reads the current world position of the robot.

		Arguments: (group)
		Arguments: ()
		:param group: The motion group number.
		:returns: The current position in world coordinates.
		'''
		__a = _bind_overload(args, kwargs, ['group'], {})
		if __a is not None:
			group, = __a
			return Position(None, None, None, None, self._instance.ReadWorldPosition(group))
		__a = _bind_overload(args, kwargs, [], {})
		if __a is not None:
			return Position(None, None, None, None, self._instance.ReadWorldPosition())
		raise TypeError("read_world_position(): no overload takes these arguments")

	@typing.overload
	def read_user_frame_position(self, userFrame: int, group: int) -> Position: ...

	@typing.overload
	def read_user_frame_position(self, userFrame: int) -> Position: ...

	def read_user_frame_position(self, *args, **kwargs) -> Position:
		'''Reads the current position in the specified user frame and motion group.
		Reads the current position in the specified user frame.

		Arguments: (userFrame, group)
		Arguments: (userFrame)
		:param userFrame: The user frame number.
		:param group: The motion group number.
		:returns: The current position in the user frame.
		'''
		__a = _bind_overload(args, kwargs, ['userFrame', 'group'], {})
		if __a is not None:
			userFrame, group = __a
			return Position(None, None, None, None, self._instance.ReadUserFramePosition(userFrame, group))
		__a = _bind_overload(args, kwargs, ['userFrame'], {})
		if __a is not None:
			userFrame, = __a
			return Position(None, None, None, None, self._instance.ReadUserFramePosition(userFrame))
		raise TypeError("read_user_frame_position(): no overload takes these arguments")

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

def _bind_overload(args, kwargs, names, defaults):
	if len(args) > len(names) or any(k not in names[len(args):] for k in kwargs):
		return None
	values = list(args)
	for name in names[len(args):]:
		if name in kwargs:
			values.append(kwargs[name])
		elif name in defaults:
			values.append(defaults[name])
		else:
			return None
	return values
