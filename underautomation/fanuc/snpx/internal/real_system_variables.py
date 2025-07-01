import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.assignment.real_system_variables_batch_assignment import RealSystemVariablesBatchAssignment
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import RealSystemVariables as real_system_variables

class RealSystemVariables(SnpxWritableAssignableElements3[float, str, RealSystemVariablesBatchAssignment]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = real_system_variables()
		else:
			self._instance = _internal
