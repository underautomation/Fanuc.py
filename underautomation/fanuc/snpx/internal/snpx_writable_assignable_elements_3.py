import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxWritableAssignableElements as snpx_writable_assignable_elements_3

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
TAssignment = typing.TypeVar('TAssignment')
class SnpxWritableAssignableElements3(SnpxAssignableElements2[TValue, TIndex], typing.Generic[TValue, TIndex, TAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_writable_assignable_elements_3()
		else:
			self._instance = _internal
	def write(self, index: TIndex, value: TValue) -> None:
		self._instance.Write(index, value)
	def create_batch_assignment(self, indexes: typing.List[TIndex]) -> TAssignment:
		return self._instance.CreateBatchAssignment(indexes)
