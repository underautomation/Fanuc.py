import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import BigallowVariableType as bigallow_variable_type

class BigallowVariableType(GenericVariableType):
	'''Describes the Fanuc type BIGALLOW_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bigallow_variable_type()
		else:
			self._instance = _internal

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def var_name(self) -> str:
		'''Value of variable $VAR_NAME'''
		return self._instance.VarName

	@property
	def index(self) -> int:
		'''Value of variable $INDEX'''
		return self._instance.Index

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BigallowVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
