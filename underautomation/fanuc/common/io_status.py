from __future__ import annotations
import typing
from underautomation.fanuc.common.digital_ports import DigitalPorts
from UnderAutomation.Fanuc.Common import IOStatus as io_status
from UnderAutomation.Fanuc.Common import DigitalPorts as digital_ports

class IOStatus:
	'''A digital port status'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_status()
		else:
			self._instance = _internal

	@property
	def port(self) -> DigitalPorts:
		'''Digital port type'''
		return DigitalPorts(int(self._instance.Port))

	@property
	def id(self) -> int:
		'''Digital port ID'''
		return self._instance.Id

	@property
	def value(self) -> bool:
		'''Digital port value'''
		return self._instance.Value

	@property
	def name(self) -> str:
		'''IO Name'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IOStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
