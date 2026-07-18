from __future__ import annotations
import typing
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiIndexedFrameResponse as rmi_indexed_frame_response

class RmiIndexedFrameResponse(RmiResponseBase):
	'''Cartesian frame data paired with an index (UFRAME or UTOOL number).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_indexed_frame_response()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''Index (UFRAME or UTOOL number).'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def frame(self) -> XYZWPRPosition:
		'''Frame data.'''
		return XYZWPRPosition(None, None, None, None, None, None, self._instance.Frame)

	@frame.setter
	def frame(self, value: XYZWPRPosition):
		self._instance.Frame = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiIndexedFrameResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
