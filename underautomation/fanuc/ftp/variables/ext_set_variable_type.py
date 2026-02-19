import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ExtSetVariableType as ext_set_variable_type

class ExtSetVariableType(GenericVariableType):
	'''Describes the Fanuc type EXT_SET_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ext_set_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def di_type(self) -> int:
		'''Value of variable $DI_TYPE'''
		return self._instance.DiType

	@property
	def di_num(self) -> int:
		'''Value of variable $DI_NUM'''
		return self._instance.DiNum

	@property
	def do_type(self) -> int:
		'''Value of variable $DO_TYPE'''
		return self._instance.DoType

	@property
	def do_num(self) -> int:
		'''Value of variable $DO_NUM'''
		return self._instance.DoNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ExtSetVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
