from __future__ import annotations
import typing
from underautomation.fanuc.snpx.internal.simulation_type import SimulationType
from UnderAutomation.Fanuc.Snpx.Internal import SimulationData as simulation_data
from UnderAutomation.Fanuc.Snpx.Internal import SimulationType as simulation_type

class SimulationData:
	'''Specifies the I/O type and index for reading or writing simulation status via SNPX.'''
	def __init__(self, type: SimulationType, index: int, _internal = 0):
		'''Creates a new instance with the specified type and index.

		:param type: The type of I/O.
		:param index: The 1-based index of the I/O.
		'''
		if(_internal == 0):
			self._instance = simulation_data(type, index)
		else:
			self._instance = _internal

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	@property
	def type(self) -> SimulationType:
		'''The type of I/O.'''
		return SimulationType(int(self._instance.Type))

	@type.setter
	def type(self, value: SimulationType):
		self._instance.Type = simulation_type(int(value))

	@property
	def index(self) -> int:
		'''The 1-based index of the I/O. Must be >= 1.'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SimulationData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
