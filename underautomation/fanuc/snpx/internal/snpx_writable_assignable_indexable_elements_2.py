import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxWritableAssignableIndexableElements as snpx_writable_assignable_indexable_elements_2

TValue = typing.TypeVar('TValue')
TAssignment = typing.TypeVar('TAssignment')
class SnpxWritableAssignableIndexableElements2(SnpxWritableAssignableElements3[TValue, int, TAssignment], typing.Generic[TValue, TAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_writable_assignable_indexable_elements_2()
		else:
			self._instance = _internal
	def create_batch_assignment(self, startIndex: int, count: int) -> TAssignment:
		return self._instance.CreateBatchAssignment(startIndex, count)
