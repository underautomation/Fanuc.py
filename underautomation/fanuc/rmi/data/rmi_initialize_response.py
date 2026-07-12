from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiInitializeResponse as rmi_initialize_response

class RmiInitializeResponse(RmiResponseBase):
	'''Response to the Initialize command, which starts the RMI motion program on the controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_initialize_response()
		else:
			self._instance = _internal

	@property
	def group_mask(self) -> int | None:
		'''Motion group mask echoed back by the controller. null when the controller does not return this field (single-group systems or MajorVersion < 2).'''
		return self._instance.GroupMask

	@group_mask.setter
	def group_mask(self, value: int | None):
		self._instance.GroupMask = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiInitializeResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
