import typing
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionConnectParametersBase as stream_motion_connect_parameters_base

class StreamMotionConnectParametersBase:
	'''Base connection parameters for Stream Motion (J519)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_connect_parameters_base()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def port(self) -> int:
		'''UDP port for Stream Motion communication'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def send_timeout_ms(self) -> int:
		'''Send timeout in milliseconds'''
		return self._instance.SendTimeoutMs

	@send_timeout_ms.setter
	def send_timeout_ms(self, value: int):
		self._instance.SendTimeoutMs = value

	@property
	def receive_timeout_ms(self) -> int:
		'''Receive timeout in milliseconds'''
		return self._instance.ReceiveTimeoutMs

	@receive_timeout_ms.setter
	def receive_timeout_ms(self, value: int):
		self._instance.ReceiveTimeoutMs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default UDP port for Stream Motion (J519)
StreamMotionConnectParametersBase.DEFAULT_PORT = stream_motion_connect_parameters_base.DEFAULT_PORT

# Default send timeout in milliseconds
StreamMotionConnectParametersBase.DEFAULT_SEND_TIMEOUT_MS = stream_motion_connect_parameters_base.DEFAULT_SEND_TIMEOUT_MS

# Default receive timeout in milliseconds
StreamMotionConnectParametersBase.DEFAULT_RECEIVE_TIMEOUT_MS = stream_motion_connect_parameters_base.DEFAULT_RECEIVE_TIMEOUT_MS
