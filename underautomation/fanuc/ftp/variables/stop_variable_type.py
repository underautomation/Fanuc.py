import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import StopVariableType as stop_variable_type

class StopVariableType(GenericVariableType):
	'''Describes the Fanuc type $STOP'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stop_variable_type()
		else:
			self._instance = _internal

	@property
	def tick(self) -> int:
		'''Value of variable $TICK'''
		return self._instance.Tick

	@property
	def spd(self) -> float:
		'''Value of variable $SPD'''
		return self._instance.Spd

	@property
	def pos1(self) -> float:
		'''Value of variable $POS1'''
		return self._instance.Pos1

	@property
	def pos2(self) -> float:
		'''Value of variable $POS2'''
		return self._instance.Pos2

	@property
	def pos3(self) -> float:
		'''Value of variable $POS3'''
		return self._instance.Pos3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StopVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
