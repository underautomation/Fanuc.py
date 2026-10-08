from __future__ import annotations
import typing
from underautomation.fanuc.snpx.assignment.string_registers_batch_assignment import StringRegistersBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import StringRegisters as string_registers

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class StringRegisters(SnpxWritableAssignableIndexableElements2[str, StringRegistersBatchAssignment]):
	'''Provides access to string registers (SR[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_registers()
		else:
			self._instance = _internal

	def create_batch_assignment(self, startIndex: int, count: int) -> StringRegistersBatchAssignment:
		'''Creates a batch assignment for reading multiple string registers.

		:param startIndex: The starting register index.
		:param count: The number of consecutive registers.
		:returns: A batch assignment for the specified range.
		'''
		__r = self._instance.CreateBatchAssignment(startIndex, count)
		return None if __r is None else StringRegistersBatchAssignment(__r)

	@staticmethod
	def _get_string_length() -> int:
		'''Number of characters for string register reads/writes. Must be even, greater than 2, and less than ushort.MaxValue. Warning: this static value must be set before any string register read/write and must not be changed while the SDK is running. Default: 80.'''
		return string_registers.StringLength

	@staticmethod
	def _set_string_length(value: int):
		string_registers.StringLength = value

	string_length = _StaticProperty(_get_string_length, _set_string_length)
	del _get_string_length, _set_string_length

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringRegisters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
