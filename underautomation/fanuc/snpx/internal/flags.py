import typing
from underautomation.fanuc.snpx.assignment.flag_batch_assignment import FlagBatchAssignment
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import Flags as flags

class Flags(SnpxWritableAssignableIndexableElements2[bool, FlagBatchAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flags()
		else:
			self._instance = _internal
	def create_batch_assignment(self, startIndex: int, count: int) -> FlagBatchAssignment:
		return FlagBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))
