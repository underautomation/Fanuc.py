from __future__ import annotations
import typing
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from UnderAutomation.Fanuc.Rmi.Data import RmiRecordedCartesianPosition as rmi_recorded_cartesian_position

class RmiRecordedCartesianPosition:
	'''Cartesian position received from the controller via the RMI Position Record menu (TouchUp).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_recorded_cartesian_position()
		else:
			self._instance = _internal

	@property
	def position_id(self) -> int:
		'''Position identifier assigned by the controller.'''
		return self._instance.PositionId

	@position_id.setter
	def position_id(self, value: int):
		self._instance.PositionId = value

	@property
	def position(self) -> CartesianPositionWithUserFrame:
		'''Recorded Cartesian position including arm configuration and active frame/tool numbers.'''
		return CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, self._instance.Position)

	@position.setter
	def position(self, value: CartesianPositionWithUserFrame):
		self._instance.Position = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiRecordedCartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
