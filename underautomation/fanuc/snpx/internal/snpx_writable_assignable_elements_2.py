import typing
from underautomation.fanuc.snpx.internal.snpx_assignable_elements_2 import SnpxAssignableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxWritableAssignableElements as snpx_writable_assignable_elements_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class SnpxWritableAssignableElements2(SnpxAssignableElements2[TValue, TIndex], typing.Generic[TValue, TIndex]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_writable_assignable_elements_2()
		else:
			self._instance = _internal
	def write(self, index: TIndex, value: TValue) -> None:
		self._instance.Write(index, value)
