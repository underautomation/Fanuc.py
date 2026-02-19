import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AlmdgVariableType as almdg_variable_type

class AlmdgVariableType(GenericVariableType):
	'''Describes the Fanuc type ALMDG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = almdg_variable_type()
		else:
			self._instance = _internal

	@property
	def debug1(self) -> int:
		'''Value of variable $DEBUG1'''
		return self._instance.Debug1

	@property
	def debug2(self) -> int:
		'''Value of variable $DEBUG2'''
		return self._instance.Debug2

	@property
	def debug3(self) -> int:
		'''Value of variable $DEBUG3'''
		return self._instance.Debug3

	@property
	def cont_type(self) -> int:
		'''Value of variable $CONT_TYPE'''
		return self._instance.ContType

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AlmdgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
