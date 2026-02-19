import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SnpxAsgVariableType as snpx_asg_variable_type

class SnpxAsgVariableType(GenericVariableType):
	'''Describes the Fanuc type SNPX_ASG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_asg_variable_type()
		else:
			self._instance = _internal

	@property
	def address(self) -> int:
		'''Value of variable $ADDRESS'''
		return self._instance.Address

	@property
	def size(self) -> int:
		'''Value of variable $SIZE'''
		return self._instance.Size

	@property
	def var_name(self) -> str:
		'''Value of variable $VAR_NAME'''
		return self._instance.VarName

	@property
	def multiply(self) -> float:
		'''Value of variable $MULTIPLY'''
		return self._instance.Multiply

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxAsgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
