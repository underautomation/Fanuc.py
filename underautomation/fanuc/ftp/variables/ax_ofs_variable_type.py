import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AxOfsVariableType as ax_ofs_variable_type

class AxOfsVariableType(GenericVariableType):
	'''Describes the Fanuc type AX_OFS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ax_ofs_variable_type()
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''Value of variable $X'''
		return self._instance.X

	@property
	def y(self) -> float:
		'''Value of variable $Y'''
		return self._instance.Y

	@property
	def z(self) -> float:
		'''Value of variable $Z'''
		return self._instance.Z

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AxOfsVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
