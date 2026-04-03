from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common.Files import OnProgressDelegate as on_progress_delegate

class OnProgressDelegate:
	'''Delegate to track File transfer progress. The value provided is in the range 0 to 100'''
	def __init__(self, object: typing.Any, method: typing.Any, _internal = 0):
		if(_internal == 0):
			self._instance = on_progress_delegate(object, method)
		else:
			self._instance = _internal

	def invoke(self, progress: float) -> None:
		self._instance.Invoke(progress)

	def begin_invoke(self, progress: float, callback: typing.Any, object: typing.Any) -> typing.Any:
		return self._instance.BeginInvoke(progress, callback, object)

	def end_invoke(self, result: typing.Any) -> None:
		self._instance.EndInvoke(result)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, OnProgressDelegate):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
