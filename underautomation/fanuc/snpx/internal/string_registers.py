import typing
from underautomation.fanuc.snpx.assignment.string_registers_batch_assignment import StringRegistersBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import StringRegisters as string_registers

class StringRegisters(SnpxWritableAssignableIndexableElements2[str, StringRegistersBatchAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_registers()
		else:
			self._instance = _internal
	def create_batch_assignment(self, startIndex: int, count: int) -> StringRegistersBatchAssignment:
		return StringRegistersBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))
