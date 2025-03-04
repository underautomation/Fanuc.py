import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcalMvVariableType as vcal_mv_variable_type

class VcalMvVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_mv_variable_type()
		else:
			self._instance = _internal
	@property
	def rob_group(self) -> int:
		return self._instance.RobGroup
	@property
	def command_pos(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CommandPos)
	@property
	def vs_speed(self) -> float:
		return self._instance.VsSpeed
	@property
	def max_rdelay(self) -> int:
		return self._instance.MaxRdelay
	@property
	def rob_axis(self) -> float:
		return self._instance.RobAxis
	@property
	def motype(self) -> int:
		return self._instance.Motype
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
