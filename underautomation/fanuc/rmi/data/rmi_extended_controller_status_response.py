from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiExtendedControllerStatusResponse as rmi_extended_controller_status_response

class RmiExtendedControllerStatusResponse(RmiResponseBase):
	'''Extended controller status returned by FRC_GetExtStatus.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_extended_controller_status_response()
		else:
			self._instance = _internal

	@property
	def error_code(self) -> str:
		'''Last reported error code text, or null when no error is active.'''
		return self._instance.ErrorCode

	@error_code.setter
	def error_code(self, value: str):
		self._instance.ErrorCode = value

	@property
	def in_motion(self) -> bool:
		'''Whether the robot is currently executing a motion.'''
		return self._instance.InMotion

	@in_motion.setter
	def in_motion(self, value: bool):
		self._instance.InMotion = value

	@property
	def control_mode(self) -> str:
		'''Active control mode string (e.g. "AUTO"), or null when unavailable.'''
		return self._instance.ControlMode

	@control_mode.setter
	def control_mode(self, value: str):
		self._instance.ControlMode = value

	@property
	def drives_powered(self) -> bool:
		'''Whether the servo drives are powered on.'''
		return self._instance.DrivesPowered

	@drives_powered.setter
	def drives_powered(self, value: bool):
		self._instance.DrivesPowered = value

	@property
	def gen_override(self) -> int:
		'''General speed override percentage.'''
		return self._instance.GenOverride

	@gen_override.setter
	def gen_override(self, value: int):
		self._instance.GenOverride = value

	@property
	def speed_clamp_limit(self) -> float | None:
		'''Speed clamp limit in mm/s, or null when not configured.'''
		return self._instance.SpeedClampLimit

	@speed_clamp_limit.setter
	def speed_clamp_limit(self, value: float | None):
		self._instance.SpeedClampLimit = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiExtendedControllerStatusResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
