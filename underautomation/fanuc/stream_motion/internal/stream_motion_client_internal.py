import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_client_base import StreamMotionClientBase
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionClientInternal as stream_motion_client_internal

class StreamMotionClientInternal(StreamMotionClientBase):
	'''Internal Stream Motion client for use within FanucRobot'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
