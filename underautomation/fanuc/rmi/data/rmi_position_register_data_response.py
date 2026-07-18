from __future__ import annotations
import typing
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiPositionRegisterDataResponse as rmi_position_register_data_response

class RmiPositionRegisterDataResponse(RmiResponseBase):
	'''Position register data paired with its register number.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_position_register_data_response()
		else:
			self._instance = _internal

	@property
	def register_number(self) -> int:
		'''Register number'''
		return self._instance.RegisterNumber

	@register_number.setter
	def register_number(self, value: int):
		self._instance.RegisterNumber = value

	@property
	def cartesian_position(self) -> CartesianPositionWithUserFrame:
		'''Position register value.'''
		return CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, self._instance.CartesianPosition)

	@cartesian_position.setter
	def cartesian_position(self, value: CartesianPositionWithUserFrame):
		self._instance.CartesianPosition = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiPositionRegisterDataResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
