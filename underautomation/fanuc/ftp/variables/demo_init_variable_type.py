import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DemoInitVariableType as demo_init_variable_type

class DemoInitVariableType(GenericVariableType):
	'''Describes the Fanuc type DEMO_INIT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = demo_init_variable_type()
		else:
			self._instance = _internal

	@property
	def demo_enb(self) -> bool:
		'''Value of variable $DEMO_ENB'''
		return self._instance.DemoEnb

	@property
	def demo_au(self) -> bool:
		'''Value of variable $DEMO_AU'''
		return self._instance.DemoAu

	@property
	def demo_days(self) -> int:
		'''Value of variable $DEMO_DAYS'''
		return self._instance.DemoDays

	@property
	def load_num(self) -> int:
		'''Value of variable $LOAD_NUM'''
		return self._instance.LoadNum

	@property
	def dummy4(self) -> int:
		'''Value of variable $DUMMY4'''
		return self._instance.Dummy4

	@property
	def dummy5(self) -> int:
		'''Value of variable $DUMMY5'''
		return self._instance.Dummy5

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DemoInitVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
