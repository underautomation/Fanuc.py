import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ReclocVariableType as recloc_variable_type

class ReclocVariableType(GenericVariableType):
	'''Describes the Fanuc type RECLOC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = recloc_variable_type()
		else:
			self._instance = _internal

	@property
	def slots(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $SLOTS'''
		return [CartesianPositionVariable(x) for x in self._instance.Slots]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReclocVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
