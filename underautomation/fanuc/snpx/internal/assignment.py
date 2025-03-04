import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import Assignment as assignment

class Assignment:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = assignment()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def offset(self) -> int:
		return self._instance.Offset
	@property
	def is_assignment_cleared(self) -> bool:
		return self._instance.IsAssignmentCleared
	@property
	def name(self) -> str:
		return self._instance.Name
