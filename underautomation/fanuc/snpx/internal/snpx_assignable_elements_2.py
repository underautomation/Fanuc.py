import typing
from underautomation.fanuc.snpx.internal.assignment_1 import Assignment1
from underautomation.fanuc.snpx.internal.snpx_elements_2 import SnpxElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxAssignableElements as snpx_assignable_elements_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class SnpxAssignableElements2(SnpxElements2[TValue, TIndex], typing.Generic[TValue, TIndex]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_assignable_elements_2()
		else:
			self._instance = _internal
	def read(self, index: TIndex) -> TValue:
		return self._instance.Read(index)
	def get_or_create_assignment(self, index: TIndex) -> Assignment1[TIndex]:
		return Assignment1[TIndex](self._instance.GetOrCreateAssignment(index))
