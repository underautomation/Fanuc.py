import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_client_base import StreamMotionClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionClientInternal as stream_motion_client_internal

class StreamMotionClientInternal(StreamMotionClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_client_internal()
		else:
			self._instance = _internal
