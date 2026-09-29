from __future__ import annotations
import typing
from underautomation.fanuc.stream_motion.stream_motion_error import StreamMotionError
from UnderAutomation.Fanuc.StreamMotion import StreamMotionException as stream_motion_exception
from UnderAutomation.Fanuc.StreamMotion import StreamMotionError as stream_motion_error

class StreamMotionException:
	'''Error raised by the Stream Motion client'''
	def __init__(self, error: StreamMotionError, message: str, inner: typing.Any, _internal = 0):
		'''Creates a Stream Motion exception with an inner exception

		:param error: Kind of error
		:param message: Error message
		:param inner: Inner exception
		'''
		if(_internal == 0):
			self._instance = stream_motion_exception(stream_motion_error(int(error)), message, inner)
		else:
			self._instance = _internal

	@property
	def error(self) -> StreamMotionError:
		'''Kind of error'''
		return StreamMotionError(int(self._instance.Error))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
