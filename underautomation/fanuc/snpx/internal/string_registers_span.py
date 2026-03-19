import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.internal.string_register_span import StringRegisterSpan
from underautomation.fanuc.snpx.assignment.string_registers_span_batch_assignment import StringRegistersSpanBatchAssignment
from UnderAutomation.Fanuc.Snpx.Internal import StringRegistersSpan as string_registers_span

class StringRegistersSpan(SnpxWritableAssignableElements3[str, StringRegisterSpan, StringRegistersSpanBatchAssignment]):
	'''Provides access to string registers (SR[]) with control over start index and length via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_registers_span()
		else:
			self._instance = _internal

	def read(self, registerIndex: int, stringLength: int, stringStartIndex: int=0) -> str:
		'''Reads a substring from the specified string register.

		:param registerIndex: The register index (1-based).
		:param stringLength: The number of characters to read (must be even, >= 2).
		:param stringStartIndex: The start index within the string (must be even, >= 0).
		:returns: The string value read from the register.
		'''
		return self._instance.Read(registerIndex, stringLength, stringStartIndex)

	def write(self, registerIndex: int, value: str, stringLength: int, stringStartIndex: int=0) -> None:
		'''Writes a string value to the specified string register span.

		:param registerIndex: The register index (1-based).
		:param value: The string value to write.
		:param stringLength: The number of characters to write (must be even, >= 2).
		:param stringStartIndex: The start index within the string (must be even, >= 0).
		'''
		self._instance.Write(registerIndex, value, stringLength, stringStartIndex)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringRegistersSpan):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
