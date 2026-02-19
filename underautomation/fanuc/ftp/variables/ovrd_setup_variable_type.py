import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import OvrdSetupVariableType as ovrd_setup_variable_type

class OvrdSetupVariableType(GenericVariableType):
	'''Describes the Fanuc type OVRD_SETUP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ovrd_setup_variable_type()
		else:
			self._instance = _internal

	@property
	def ovrd_num(self) -> int:
		'''Value of variable $OVRD_NUM'''
		return self._instance.OvrdNum

	@property
	def override(self) -> typing.List[int]:
		'''Value of variable $OVERRIDE'''
		return self._instance.Override

	@property
	def ovrd_num_s(self) -> int:
		'''Value of variable $OVRD_NUM_S'''
		return self._instance.OvrdNumS

	@property
	def override_s(self) -> typing.List[int]:
		'''Value of variable $OVERRIDE_S'''
		return self._instance.OverrideS

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, OvrdSetupVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
