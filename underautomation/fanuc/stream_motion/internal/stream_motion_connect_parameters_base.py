import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Internal import StreamMotionConnectParametersBase as stream_motion_connect_parameters_base

class StreamMotionConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def send_timeout_ms(self) -> int:
		return self._instance.SendTimeoutMs
	@send_timeout_ms.setter
	def send_timeout_ms(self, value: int):
		self._instance.SendTimeoutMs = value
	@property
	def receive_timeout_ms(self) -> int:
		return self._instance.ReceiveTimeoutMs
	@receive_timeout_ms.setter
	def receive_timeout_ms(self, value: int):
		self._instance.ReceiveTimeoutMs = value

StreamMotionConnectParametersBase.defaul_t__port = StreamMotionConnectParametersBase(stream_motion_connect_parameters_base.DEFAULT_PORT)

StreamMotionConnectParametersBase.defaul_t__sen_d__timeou_t__ms = StreamMotionConnectParametersBase(stream_motion_connect_parameters_base.DEFAULT_SEND_TIMEOUT_MS)

StreamMotionConnectParametersBase.defaul_t__receiv_e__timeou_t__ms = StreamMotionConnectParametersBase(stream_motion_connect_parameters_base.DEFAULT_RECEIVE_TIMEOUT_MS)
