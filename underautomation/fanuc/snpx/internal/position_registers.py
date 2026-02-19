import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.snpx.assignment.position_registers_batch_assignment import PositionRegistersBatchAssignment
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_indexable_elements_2 import SnpxWritableAssignableIndexableElements2
from UnderAutomation.Fanuc.Snpx.Internal import PositionRegisters as position_registers

class PositionRegisters(SnpxWritableAssignableIndexableElements2[Position, PositionRegistersBatchAssignment]):
	'''Provides access to position registers (PR[]) on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = position_registers()
		else:
			self._instance = _internal

	def write(self, index: int, cartesianPosition: CartesianPosition) -> None:
		'''Writes a Cartesian position to the specified position register.

		:param index: The register index.
		:param cartesianPosition: The Cartesian position to write.
		'''
		self._instance.Write(index, cartesianPosition._instance if cartesianPosition else None)

	def create_batch_assignment(self, startIndex: int, count: int) -> PositionRegistersBatchAssignment:
		'''Creates a batch assignment for reading multiple position registers.

		:param startIndex: The starting register index.
		:param count: The number of consecutive registers.
		:returns: A batch assignment for the specified range.
		'''
		return PositionRegistersBatchAssignment(self._instance.CreateBatchAssignment(startIndex, count))

	def read(self, index: int) -> Position:
		'''Reads the position at the specified register index.

		:param index: The register index.
		:returns: The position value.
		'''
		return Position(None, None, None, None, self._instance.Read(index))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PositionRegisters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
