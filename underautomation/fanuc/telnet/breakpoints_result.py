import typing
from underautomation.fanuc.telnet.breakpoint import Breakpoint
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import BreakpointsResult as breakpoints_result

class BreakpointsResult(Result):
	'''Result containing the breakpoints of a task.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = breakpoints_result()
		else:
			self._instance = _internal

	@property
	def breakpoints(self) -> typing.List[Breakpoint]:
		'''Gets the breakpoints set on the task.'''
		return [Breakpoint(x) for x in self._instance.Breakpoints]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BreakpointsResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
