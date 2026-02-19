import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CustommenuVariableType as custommenu_variable_type

class CustommenuVariableType(GenericVariableType):
	'''Describes the Fanuc type CUSTOMMENU_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = custommenu_variable_type()
		else:
			self._instance = _internal

	@property
	def title(self) -> str:
		'''Value of variable $TITLE'''
		return self._instance.Title

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def option(self) -> int:
		'''Value of variable $OPTION'''
		return self._instance.Option

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CustommenuVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
