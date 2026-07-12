from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Rmi.Data import RmiSetPayloadCompensationParameters as rmi_set_payload_compensation_parameters

class RmiSetPayloadCompensationParameters:
	'''Parameters for defining payload compensation for a payload schedule. Used by RmiSetPayloadCompensationParameters). All positional values are in meters; mass in kg; inertia in kg·m².'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_set_payload_compensation_parameters()
		else:
			self._instance = _internal

	@property
	def schedule_number(self) -> int:
		'''Payload schedule number to configure.'''
		return self._instance.ScheduleNumber

	@schedule_number.setter
	def schedule_number(self, value: int):
		self._instance.ScheduleNumber = value

	@property
	def mass_kg(self) -> float:
		'''Payload mass in kilograms.'''
		return self._instance.MassKg

	@mass_kg.setter
	def mass_kg(self, value: float):
		self._instance.MassKg = value

	@property
	def cg_xm(self) -> float:
		'''Center-of-gravity X offset in meters.'''
		return self._instance.CgXm

	@cg_xm.setter
	def cg_xm(self, value: float):
		self._instance.CgXm = value

	@property
	def cg_ym(self) -> float:
		'''Center-of-gravity Y offset in meters.'''
		return self._instance.CgYm

	@cg_ym.setter
	def cg_ym(self, value: float):
		self._instance.CgYm = value

	@property
	def cg_zm(self) -> float:
		'''Center-of-gravity Z offset in meters.'''
		return self._instance.CgZm

	@cg_zm.setter
	def cg_zm(self, value: float):
		self._instance.CgZm = value

	@property
	def inertia_xkgm2(self) -> float:
		'''Inertia around the X axis in kg·m².'''
		return self._instance.InertiaXkgm2

	@inertia_xkgm2.setter
	def inertia_xkgm2(self, value: float):
		self._instance.InertiaXkgm2 = value

	@property
	def inertia_ykgm2(self) -> float:
		'''Inertia around the Y axis in kg·m².'''
		return self._instance.InertiaYkgm2

	@inertia_ykgm2.setter
	def inertia_ykgm2(self, value: float):
		self._instance.InertiaYkgm2 = value

	@property
	def inertia_zkgm2(self) -> float:
		'''Inertia around the Z axis in kg·m².'''
		return self._instance.InertiaZkgm2

	@inertia_zkgm2.setter
	def inertia_zkgm2(self, value: float):
		self._instance.InertiaZkgm2 = value

	@property
	def group(self) -> int | None:
		'''Optional motion group number. null uses the active group.'''
		return self._instance.Group

	@group.setter
	def group(self, value: int | None):
		self._instance.Group = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiSetPayloadCompensationParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
