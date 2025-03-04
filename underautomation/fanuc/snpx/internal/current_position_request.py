import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import CurrentPositionRequest as current_position_request

class CurrentPositionRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position_request()
		else:
			self._instance = _internal
	@property
	def group(self) -> int:
		return self._instance.Group
	@group.setter
	def group(self, value: int):
		self._instance.Group = value
	@property
	def user_frame(self) -> int:
		return self._instance.UserFrame
	@user_frame.setter
	def user_frame(self, value: int):
		self._instance.UserFrame = value
