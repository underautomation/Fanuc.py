from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiUFrameUToolNumbersResponse as rmi_u_frame_u_tool_numbers_response

class RmiUFrameUToolNumbersResponse(RmiResponseBase):
	'''Current UFRAME and UTOOL numbers, optionally scoped to a motion group.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_u_frame_u_tool_numbers_response()
		else:
			self._instance = _internal

	@property
	def frame(self) -> int:
		'''Current user frame number.'''
		return self._instance.Frame

	@frame.setter
	def frame(self, value: int):
		self._instance.Frame = value

	@property
	def tool(self) -> int:
		'''Current user tool number.'''
		return self._instance.Tool

	@tool.setter
	def tool(self, value: int):
		self._instance.Tool = value

	@property
	def group(self) -> int | None:
		'''Motion group number, or null when not applicable.'''
		return self._instance.Group

	@group.setter
	def group(self, value: int | None):
		self._instance.Group = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiUFrameUToolNumbersResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
