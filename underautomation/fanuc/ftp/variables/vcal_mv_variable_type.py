import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcalMvVariableType as vcal_mv_variable_type

class VcalMvVariableType(GenericVariableType):
	'''Describes the Fanuc type VCAL_MV_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_mv_variable_type()
		else:
			self._instance = _internal

	@property
	def rob_group(self) -> int:
		'''Value of variable ROB_GROUP'''
		return self._instance.RobGroup

	@property
	def command_pos(self) -> CartesianPositionVariable:
		'''Value of variable COMMAND_POS'''
		return CartesianPositionVariable(self._instance.CommandPos)

	@property
	def vs_speed(self) -> float:
		'''Value of variable VS_SPEED'''
		return self._instance.VsSpeed

	@property
	def max_rdelay(self) -> int:
		'''Value of variable MAX_RDELAY'''
		return self._instance.MaxRdelay

	@property
	def rob_axis(self) -> float:
		'''Value of variable ROB_AXIS'''
		return self._instance.RobAxis

	@property
	def motype(self) -> int:
		'''Value of variable MOTYPE'''
		return self._instance.Motype

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcalMvVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
