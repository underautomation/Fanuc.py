import typing
from underautomation.fanuc.snpx.internal.assignment_1 import Assignment1
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import BatchAssignment as batch_assignment_2

TValue = typing.TypeVar('TValue')
TIndex = typing.TypeVar('TIndex')
class BatchAssignment2(typing.Generic[TValue, TIndex]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = batch_assignment_2()
		else:
			self._instance = _internal
	def read(self) -> typing.List[TValue]:
		return list(self._instance.Read())
	@property
	def assignments(self) -> typing.List[Assignment1]:
		return [Assignment1(x) for x in self._instance.Assignments]
	@assignments.setter
	def assignments(self, value: typing.List[Assignment1]):
		self._instance.Assignments = value
