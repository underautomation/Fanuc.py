import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.assignment.string_system_variables_batch_assignment import StringSystemVariablesBatchAssignment
from UnderAutomation.Fanuc.Snpx.Internal import StringSystemVariables as string_system_variables

class StringSystemVariables(SnpxWritableAssignableElements3[str, str, StringSystemVariablesBatchAssignment]):
	'''Provides access to string system variables on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_system_variables()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringSystemVariables):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
