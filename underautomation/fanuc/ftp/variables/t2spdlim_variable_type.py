import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import T2spdlimVariableType as t2spdlim_variable_type

class T2spdlimVariableType(GenericVariableType):
	'''Describes the Fanuc type T2SPDLIM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = t2spdlim_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def use_taskid(self) -> int:
		'''Value of variable $USE_TASKID'''
		return self._instance.UseTaskid

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, T2spdlimVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
