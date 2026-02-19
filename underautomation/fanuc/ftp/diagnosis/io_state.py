import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.common.io_status import IOStatus
from UnderAutomation.Fanuc.Ftp.Diagnosis import IOState as io_state

class IOState(IFanucContent):
	'''Status of all controller inputs and outputs'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_state()
		else:
			self._instance = _internal

	@property
	def states(self) -> typing.List[IOStatus]:
		'''Status of all controller inputs and outputs'''
		return [IOStatus(x) for x in self._instance.States]

	@property
	def name(self) -> str:
		'''File name : iostate.dg'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
