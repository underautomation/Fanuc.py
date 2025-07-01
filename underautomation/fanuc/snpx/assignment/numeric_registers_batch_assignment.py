import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Assignment import NumericRegistersBatchAssignment as numeric_registers_batch_assignment

class NumericRegistersBatchAssignment(BatchAssignment2[float, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_registers_batch_assignment()
		else:
			self._instance = _internal
	def read(self) -> typing.List[float]:
		return self._instance.Read()
