import typing
from __future__ import annotation
from underautomation.fanuc.snpx.internal.simulation_type import SimulationType
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.internal.simulation_data import SimulationData
from underautomation.fanuc.snpx.assignment.simulation_status_batch_assignment import SimulationStatusBatchAssignment
from UnderAutomation.Fanuc.Snpx.Internal import SimulationStatus as simulation_status
from UnderAutomation.Fanuc.Snpx.Internal import SimulationType as simulation_type

class SimulationStatus(SnpxWritableAssignableElements3[bool, SimulationData, SimulationStatusBatchAssignment]):
	'''Provides read/write access to I/O simulation status via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = simulation_status()
		else:
			self._instance = _internal

	def read(self, type: SimulationType, index: int) -> bool:
		'''Reads the simulation status for the specified I/O type and index.

		:param type: The type of I/O.
		:param index: The 1-based I/O index.
		:returns: True if the I/O is simulated, false otherwise.
		'''
		return self._instance.Read(simulation_type(int(type)), index)

	def write(self, type: SimulationType, index: int, value: bool) -> None:
		'''Sets the simulation status for the specified I/O type and index.

		:param type: The type of I/O.
		:param index: The 1-based I/O index.
		:param value: True to enable simulation, false to disable.
		'''
		self._instance.Write(simulation_type(int(type)), index, value)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SimulationStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
