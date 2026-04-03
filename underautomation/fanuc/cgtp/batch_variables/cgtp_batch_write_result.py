from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpBatchWriteResult as cgtp_batch_write_result

class CgtpBatchWriteResult:
	'''Result of a batch write operation.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_batch_write_result()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpBatchWriteResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
