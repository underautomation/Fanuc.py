from __future__ import annotations
import typing
from UnderAutomation.Fanuc.StreamMotion.Data import StreamMotionErrorEventArgs as stream_motion_error_event_args

class StreamMotionErrorEventArgs:
	'''Arguments of the ErrorOccurred event'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_error_event_args()
		else:
			self._instance = _internal

	@property
	def exception(self) -> typing.Any:
		'''Error that occurred'''
		return self._instance.Exception

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionErrorEventArgs):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
