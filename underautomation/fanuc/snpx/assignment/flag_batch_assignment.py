import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Assignment import FlagBatchAssignment as flag_batch_assignment

class FlagBatchAssignment(BatchAssignment2[bool, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flag_batch_assignment()
		else:
			self._instance = _internal
	def read(self) -> typing.List[bool]:
		return self._instance.Read()
