import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RestartVariableType as restart_variable_type

class RestartVariableType(GenericVariableType):
	'''Describes the Fanuc type RESTART_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = restart_variable_type()
		else:
			self._instance = _internal

	@property
	def flag(self) -> bool:
		'''Value of variable $FLAG'''
		return self._instance.Flag

	@property
	def dsb_signal(self) -> int:
		'''Value of variable $DSB_SIGNAL'''
		return self._instance.DsbSignal

	@property
	def startup_cnd(self) -> int:
		'''Value of variable $STARTUP_CND'''
		return self._instance.StartupCnd

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RestartVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
