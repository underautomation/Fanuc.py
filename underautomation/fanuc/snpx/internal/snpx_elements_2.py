import typing
from UnderAutomation.Fanuc.Snpx.Internal import SnpxElements as snpx_elements_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class SnpxElements2(typing.Generic[TValue, TIndex]):
	'''Abstract base class for accessing SNPX elements by index.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_elements_2()
		else:
			self._instance = _internal

	def read(self, index: TIndex) -> TValue:
		'''Reads the value at the specified index.

		:param index: The index to read from.
		:returns: The value at the index.
		'''
		return self._instance.Read(index)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxElements2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
