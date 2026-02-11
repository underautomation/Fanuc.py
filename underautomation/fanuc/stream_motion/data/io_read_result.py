import typing
from underautomation.fanuc.stream_motion.data.io_type import IOType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import IOReadResult as io_read_result
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class IOReadResult:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_read_result()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def type(self) -> IOType:
		return IOType(self._instance.Type)
	@property
	def index(self) -> int:
		return self._instance.Index
	@property
	def mask(self) -> int:
		return self._instance.Mask
	@property
	def value(self) -> int:
		return self._instance.Value
