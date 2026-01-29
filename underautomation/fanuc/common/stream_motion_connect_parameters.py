import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_connect_parameters_base import StreamMotionConnectParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import StreamMotionConnectParameters as stream_motion_connect_parameters

class StreamMotionConnectParameters(StreamMotionConnectParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
	@property
	def ip(self) -> str:
		return self._instance.Ip
	@ip.setter
	def ip(self, value: str):
		self._instance.Ip = value
