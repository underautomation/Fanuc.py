import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SimiofwdlmVariableType as simiofwdlm_variable_type

class SimiofwdlmVariableType(GenericVariableType):
	'''Describes the Fanuc type SIMIOFWDLM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = simiofwdlm_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def unlock_time(self) -> float:
		'''Value of variable $UNLOCK_TIME'''
		return self._instance.UnlockTime

	@property
	def unlockedtim(self) -> int:
		'''Value of variable $UNLOCKEDTIM'''
		return self._instance.Unlockedtim

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SimiofwdlmVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
