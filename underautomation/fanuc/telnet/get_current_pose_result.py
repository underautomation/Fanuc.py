import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import GetCurrentPoseResult as get_current_pose_result

class GetCurrentPoseResult(Result):
	'''Result of a get current pose command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_current_pose_result()
		else:
			self._instance = _internal

	@property
	def group(self) -> int:
		'''Group number of the current pose.'''
		return self._instance.Group

	@property
	def position(self) -> CartesianPosition:
		'''Cartesian position value of the current pose.'''
		return CartesianPosition(None, None, None, None, None, None, None, self._instance.Position)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetCurrentPoseResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
