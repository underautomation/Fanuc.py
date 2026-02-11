import typing
from underautomation.fanuc.common.digital_ports import DigitalPorts
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import IOStatus as io_status
from UnderAutomation.Fanuc.Common import DigitalPorts as digital_ports

class IOStatus:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_status()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def port(self) -> DigitalPorts:
		return DigitalPorts(self._instance.Port)
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def value(self) -> bool:
		return self._instance.Value
	@property
	def name(self) -> str:
		return self._instance.Name
