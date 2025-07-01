import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Assignment import StringSystemVariablesBatchAssignment as string_system_variables_batch_assignment

class StringSystemVariablesBatchAssignment(BatchAssignment2[str, str]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_system_variables_batch_assignment()
		else:
			self._instance = _internal
	def read(self) -> typing.List[str]:
		return self._instance.Read()
