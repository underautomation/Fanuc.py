import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_2 import SnpxWritableAssignableElements2
from underautomation.fanuc.common.position import Position
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import PositionRegisters as position_registers

class PositionRegisters(SnpxWritableAssignableElements2[Position, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = position_registers()
		else:
			self._instance = _internal
	def write(self, index: int, cartesianPosition: CartesianPosition) -> None:
		self._instance.Write(index, cartesianPosition._instance)
