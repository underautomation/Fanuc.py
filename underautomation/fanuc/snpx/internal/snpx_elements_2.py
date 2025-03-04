import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxElements as snpx_elements_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class SnpxElements2(typing.Generic[TValue, TIndex]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_elements_2()
		else:
			self._instance = _internal
	def read(self, index: TIndex) -> TValue:
		return self._instance.Read(index)
