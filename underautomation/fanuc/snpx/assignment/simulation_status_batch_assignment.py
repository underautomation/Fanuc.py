import typing
from underautomation.fanuc.snpx.internal.batch_assignment_2 import BatchAssignment2
from underautomation.fanuc.snpx.internal.simulation_data import SimulationData
from UnderAutomation.Fanuc.Snpx.Assignment import SimulationStatusBatchAssignment as simulation_status_batch_assignment

class SimulationStatusBatchAssignment(BatchAssignment2[bool, SimulationData]):
	'''Batch assignment for reading multiple I/O simulation statuses at once.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SimulationStatusBatchAssignment class.'''
		if(_internal == 0):
			self._instance = simulation_status_batch_assignment()
		else:
			self._instance = _internal

	def read(self) -> typing.List[bool]:
		'''Reads all simulation statuses assigned in this batch.

		:returns: An array of boolean values indicating simulation state.
		'''
		return self._instance.Read()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SimulationStatusBatchAssignment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
