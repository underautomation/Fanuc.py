import typing
from UnderAutomation.Fanuc.StreamMotion.Data import ReceiveErrorEventArgs as receive_error_event_args

class ReceiveErrorEventArgs:
	'''Event arguments for receive error events'''
	def __init__(self, exception: typing.Any, isStreaming: bool, _internal = 0):
		'''Creates a new instance of ReceiveErrorEventArgs

		:param exception: The exception that occurred
		:param isStreaming: Whether streaming is still active
		'''
		if(_internal == 0):
			self._instance = receive_error_event_args(exception, isStreaming)
		else:
			self._instance = _internal

	@property
	def exception(self) -> typing.Any:
		'''The exception that occurred during receiving'''
		return self._instance.Exception

	@property
	def is_streaming(self) -> bool:
		'''Indicates whether streaming is still active after the error'''
		return self._instance.IsStreaming

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReceiveErrorEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
