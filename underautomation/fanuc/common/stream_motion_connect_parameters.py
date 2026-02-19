import typing
from underautomation.fanuc.stream_motion.internal.stream_motion_connect_parameters_base import StreamMotionConnectParametersBase
from UnderAutomation.Fanuc.Common import StreamMotionConnectParameters as stream_motion_connect_parameters

class StreamMotionConnectParameters(StreamMotionConnectParametersBase):
	'''Stream Motion connection parameters (J519 option)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should enable Stream Motion for this connection (default: false)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	@property
	def ip(self) -> str:
		'''IP address of the robot for standalone Stream Motion connections'''
		return self._instance.Ip

	@ip.setter
	def ip(self, value: str):
		self._instance.Ip = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
