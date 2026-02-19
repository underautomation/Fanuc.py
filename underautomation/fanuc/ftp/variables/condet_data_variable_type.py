import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CondetDataVariableType as condet_data_variable_type

class CondetDataVariableType(GenericVariableType):
	'''Describes the Fanuc type CONDET_DATA_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_data_variable_type()
		else:
			self._instance = _internal

	@property
	def style(self) -> int:
		'''Value of variable $STYLE'''
		return self._instance.Style

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def var_name(self) -> str:
		'''Value of variable $VAR_NAME'''
		return self._instance.VarName

	@property
	def reg_num(self) -> int:
		'''Value of variable $REG_NUM'''
		return self._instance.RegNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CondetDataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
