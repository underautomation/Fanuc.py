import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.telnet.result import Result
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import GetCurrentPoseResult as get_current_pose_result

class GetCurrentPoseResult(Result):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_current_pose_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def group(self) -> int:
		return self._instance.Group
	@property
	def position(self) -> CartesianPosition:
		return CartesianPosition(None, None, None, None, None, None, None, self._instance.Position)
