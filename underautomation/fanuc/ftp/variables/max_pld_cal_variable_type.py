import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MaxPldCalVariableType as max_pld_cal_variable_type

class MaxPldCalVariableType(GenericVariableType):
	'''Describes the Fanuc type $MAX_PLD_CAL'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = max_pld_cal_variable_type()
		else:
			self._instance = _internal

	@property
	def aa(self) -> float:
		'''Value of variable $AA'''
		return self._instance.Aa

	@property
	def bb(self) -> float:
		'''Value of variable $BB'''
		return self._instance.Bb

	@property
	def cc(self) -> float:
		'''Value of variable $CC'''
		return self._instance.Cc

	@property
	def dd(self) -> float:
		'''Value of variable $DD'''
		return self._instance.Dd

	@property
	def ee(self) -> float:
		'''Value of variable $EE'''
		return self._instance.Ee

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MaxPldCalVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
