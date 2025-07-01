import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Assignment import RealSystemVariablesBatchAssignment as real_system_variables_batch_assignment

class RealSystemVariablesBatchAssignment(BatchAssignment2[float, str]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = real_system_variables_batch_assignment()
		else:
			self._instance = _internal
	def read(self) -> typing.List[float]:
		return self._instance.Read()
