import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CollectVariableType as collect_variable_type

class CollectVariableType(GenericVariableType):
	'''Describes the Fanuc type COLLECT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = collect_variable_type()
		else:
			self._instance = _internal

	@property
	def multi_prog(self) -> bool:
		'''Value of variable $MULTI_PROG'''
		return self._instance.MultiProg

	@property
	def allow_proc(self) -> bool:
		'''Value of variable $ALLOW_PROC'''
		return self._instance.AllowProc

	@property
	def fstchildren(self) -> bool:
		'''Value of variable $FSTCHILDREN'''
		return self._instance.Fstchildren

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CollectVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
