import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.common.io_status import IOStatus
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import IOState as io_state

class IOState(IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_state()
		else:
			self._instance = _internal
	@property
	def states(self) -> typing.List[IOStatus]:
		return [IOStatus(x) for x in self._instance.States]
	@property
	def name(self) -> str:
		return self._instance.Name
