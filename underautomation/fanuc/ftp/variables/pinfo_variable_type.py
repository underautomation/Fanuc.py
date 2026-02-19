import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PinfoVariableType as pinfo_variable_type

class PinfoVariableType(GenericVariableType):
	'''Describes the Fanuc type PINFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pinfo_variable_type()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def time(self) -> int:
		'''Value of variable $TIME'''
		return self._instance.Time

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PinfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
