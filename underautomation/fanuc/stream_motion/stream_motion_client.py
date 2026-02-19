import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_client_base import StreamMotionClientBase
from UnderAutomation.Fanuc.StreamMotion import StreamMotionClient as stream_motion_client

class StreamMotionClient(StreamMotionClientBase):
	'''Stream Motion client for standalone use (J519 option) Provides UDP-based real-time streaming motion control for Fanuc robots'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the Stream Motion client'''
		if(_internal == 0):
			self._instance = stream_motion_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, port: int=60015, sendTimeoutMs: int=1000, receiveTimeoutMs: int=1000) -> None:
		'''Connect to the robot using Stream Motion protocol

		:param ip: IP address of the robot
		:param port: UDP port (default: 60015)
		:param sendTimeoutMs: Send timeout in milliseconds
		:param receiveTimeoutMs: Receive timeout in milliseconds
		'''
		self._instance.Connect(ip, port, sendTimeoutMs, receiveTimeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
