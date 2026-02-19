import typing
from underautomation.fanuc.telnet.result import Result
from UnderAutomation.Fanuc.Telnet import AddBreakpointResult as add_breakpoint_result

class AddBreakpointResult(Result):
	'''Result of adding a breakpoint.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = add_breakpoint_result()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AddBreakpointResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
