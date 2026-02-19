import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpstrtchkVariableType as tpstrtchk_variable_type

class TpstrtchkVariableType(GenericVariableType):
	'''Describes the Fanuc type TPSTRTCHK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpstrtchk_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def allow_name(self) -> str:
		'''Value of variable $ALLOW_NAME'''
		return self._instance.AllowName

	@property
	def allow_line(self) -> int:
		'''Value of variable $ALLOW_LINE'''
		return self._instance.AllowLine

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpstrtchkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
