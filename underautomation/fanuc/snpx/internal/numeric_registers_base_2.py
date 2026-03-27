from __future__ import annotations
import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import NumericRegistersBase as numeric_registers_base_2

TValue = typing.TypeVar('TValue')
TAssignment = typing.TypeVar('TAssignment')
class NumericRegistersBase2(SnpxWritableAssignableIndexableElements2[TValue, TAssignment], typing.Generic[TValue, TAssignment]):
	'''Provides access to numeric registers (R[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_registers_base_2()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericRegistersBase2):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
