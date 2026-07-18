from __future__ import annotations
import typing
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
from UnderAutomation.Fanuc.Rmi.Data import RmiCartesianPositionResponse as rmi_cartesian_position_response

class RmiCartesianPositionResponse(RmiTimedResponse):
	'''Result of reading the current Cartesian position.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_cartesian_position_response()
		else:
			self._instance = _internal

	@property
	def position(self) -> CartesianPositionWithUserFrame:
		'''Current TCP position including configuration and active frame/tool numbers.'''
		return CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, self._instance.Position)

	@position.setter
	def position(self, value: CartesianPositionWithUserFrame):
		self._instance.Position = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiCartesianPositionResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
