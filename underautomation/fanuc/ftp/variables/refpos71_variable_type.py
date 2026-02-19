import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import Refpos71VariableType as refpos71_variable_type

class Refpos71VariableType(GenericVariableType):
	'''Describes the Fanuc type REFPOS71_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = refpos71_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def atperch(self) -> bool:
		'''Value of variable $ATPERCH'''
		return self._instance.Atperch

	@property
	def dout_type(self) -> int:
		'''Value of variable $DOUT_TYPE'''
		return self._instance.DoutType

	@property
	def dout_indx(self) -> int:
		'''Value of variable $DOUT_INDX'''
		return self._instance.DoutIndx

	@property
	def perchpos(self) -> typing.List[float]:
		'''Value of variable $PERCHPOS'''
		return self._instance.Perchpos

	@property
	def perchtol(self) -> typing.List[float]:
		'''Value of variable $PERCHTOL'''
		return self._instance.Perchtol

	@property
	def homepos(self) -> bool:
		'''Value of variable $HOMEPOS'''
		return self._instance.Homepos

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Refpos71VariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
