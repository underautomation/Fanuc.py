import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HwrConfigVariableType as hwr_config_variable_type

class HwrConfigVariableType(GenericVariableType):
	'''Describes the Fanuc type HWR_CONFIG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hwr_config_variable_type()
		else:
			self._instance = _internal

	@property
	def maincpu(self) -> int:
		'''Value of variable $MAINCPU'''
		return self._instance.Maincpu

	@property
	def visioncpu(self) -> int:
		'''Value of variable $VISIONCPU'''
		return self._instance.Visioncpu

	@property
	def spare1(self) -> int:
		'''Value of variable $SPARE1'''
		return self._instance.Spare1

	@property
	def spare2(self) -> int:
		'''Value of variable $SPARE2'''
		return self._instance.Spare2

	@property
	def spare3(self) -> int:
		'''Value of variable $SPARE3'''
		return self._instance.Spare3

	@property
	def spare4(self) -> int:
		'''Value of variable $SPARE4'''
		return self._instance.Spare4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HwrConfigVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
