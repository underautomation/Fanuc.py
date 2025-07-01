import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.assignment.string_system_variables_batch_assignment import StringSystemVariablesBatchAssignment
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import StringSystemVariables as string_system_variables

class StringSystemVariables(SnpxWritableAssignableElements3[str, str, StringSystemVariablesBatchAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_system_variables()
		else:
			self._instance = _internal
