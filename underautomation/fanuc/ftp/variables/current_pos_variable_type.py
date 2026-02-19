import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CurrentPosVariableType as current_pos_variable_type

class CurrentPosVariableType(GenericVariableType):
	'''Describes the Fanuc type $CURRENT_POS'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_pos_variable_type()
		else:
			self._instance = _internal

	@property
	def posxf(self) -> CartesianPositionVariable:
		'''Value of variable $POSXF'''
		return CartesianPositionVariable(self._instance.Posxf)

	@property
	def ext1(self) -> float:
		'''Value of variable $EXT1'''
		return self._instance.Ext1

	@property
	def ext2(self) -> float:
		'''Value of variable $EXT2'''
		return self._instance.Ext2

	@property
	def ext3(self) -> float:
		'''Value of variable $EXT3'''
		return self._instance.Ext3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentPosVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
