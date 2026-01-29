import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_client_base import StreamMotionClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion import StreamMotionClient as stream_motion_client

class StreamMotionClient(StreamMotionClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, port: int=60015, sendTimeoutMs: int=1000, receiveTimeoutMs: int=1000) -> None:
		self._instance.Connect(ip, port, sendTimeoutMs, receiveTimeoutMs)
