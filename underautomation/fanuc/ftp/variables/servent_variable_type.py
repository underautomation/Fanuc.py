import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ServentVariableType as servent_variable_type

class ServentVariableType(GenericVariableType):
	'''Describes the Fanuc type SERVENT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = servent_variable_type()
		else:
			self._instance = _internal

	@property
	def s_name(self) -> str:
		'''Value of variable $S_NAME'''
		return self._instance.SName

	@property
	def s_port(self) -> int:
		'''Value of variable $S_PORT'''
		return self._instance.SPort

	@property
	def s_proto(self) -> str:
		'''Value of variable $S_PROTO'''
		return self._instance.SProto

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ServentVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
