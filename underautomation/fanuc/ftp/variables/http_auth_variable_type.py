import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HttpAuthVariableType as http_auth_variable_type

class HttpAuthVariableType(GenericVariableType):
	'''Describes the Fanuc type HTTP_AUTH_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_auth_variable_type()
		else:
			self._instance = _internal

	@property
	def object(self) -> str:
		'''Value of variable $OBJECT'''
		return self._instance.Object

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def level(self) -> int:
		'''Value of variable $LEVEL'''
		return self._instance.Level

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpAuthVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
