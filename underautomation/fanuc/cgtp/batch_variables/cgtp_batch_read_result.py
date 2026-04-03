from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpBatchReadResult as cgtp_batch_read_result

class CgtpBatchReadResult:
	'''Result of a batch read operation.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_batch_read_result()
		else:
			self._instance = _internal

	@property
	def version(self) -> str:
		'''Firmware version string returned by the controller'''
		return self._instance.Version

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpBatchReadResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
