import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IntracNVariableType as intrac_n_variable_type

class IntracNVariableType(GenericVariableType):
	'''Describes the Fanuc type INTRAC_N_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = intrac_n_variable_type()
		else:
			self._instance = _internal

	@property
	def intrac_num(self) -> typing.List[int]:
		'''Value of variable $INTRAC_NUM'''
		return self._instance.IntracNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IntracNVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
