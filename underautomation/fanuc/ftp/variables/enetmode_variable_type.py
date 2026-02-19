import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import EnetmodeVariableType as enetmode_variable_type

class EnetmodeVariableType(GenericVariableType):
	'''Describes the Fanuc type ENETMODE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enetmode_variable_type()
		else:
			self._instance = _internal

	@property
	def full_duplex(self) -> bool:
		'''Value of variable $FULL_DUPLEX'''
		return self._instance.FullDuplex

	@property
	def speed(self) -> int:
		'''Value of variable $SPEED'''
		return self._instance.Speed

	@property
	def acd_enable(self) -> bool:
		'''Value of variable $ACD_ENABLE'''
		return self._instance.AcdEnable

	@property
	def throttle(self) -> bool:
		'''Value of variable $THROTTLE'''
		return self._instance.Throttle

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EnetmodeVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
