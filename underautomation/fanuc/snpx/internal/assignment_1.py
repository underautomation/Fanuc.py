import typing
from underautomation.fanuc.snpx.internal.assignment import Assignment
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import Assignment as assignment_1

TIndex = typing.TypeVar('TIndex')
class Assignment1(Assignment, typing.Generic[TIndex]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = assignment_1()
		else:
			self._instance = _internal
	@property
	def index(self) -> TIndex:
		return self._instance.Index
