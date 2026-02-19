import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.position import Position
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_3 import SnpxWritableAssignableElements3
from underautomation.fanuc.snpx.assignment.position_system_variables_batch_assignment import PositionSystemVariablesBatchAssignment
from UnderAutomation.Fanuc.Snpx.Internal import PositionSystemVariables as position_system_variables

class PositionSystemVariables(SnpxWritableAssignableElements3[Position, str, PositionSystemVariablesBatchAssignment]):
	'''Provides access to position system variables on the robot via SNPX.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = position_system_variables()
		else:
			self._instance = _internal

	def write(self, variable: str, cartesianPosition: CartesianPosition) -> None:
		'''Writes a Cartesian position to the specified system variable.

		:param variable: The system variable name.
		:param cartesianPosition: The Cartesian position to write.
		'''
		self._instance.Write(variable, cartesianPosition._instance if cartesianPosition else None)

	def read(self, index: str) -> Position:
		'''Reads the position at the specified system variable.

		:param index: The system variable name.
		:returns: The position value.
		'''
		return Position(None, None, None, None, self._instance.Read(index))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PositionSystemVariables):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
