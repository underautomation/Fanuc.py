import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UserToolVariableType as user_tool_variable_type

class UserToolVariableType(GenericVariableType):
	'''Describes the Fanuc type USER_TOOL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_tool_variable_type()
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
	def w(self) -> float:
		'''Value of variable $W'''
		return self._instance.W

	@property
	def p(self) -> float:
		'''Value of variable $P'''
		return self._instance.P

	@property
	def r(self) -> float:
		'''Value of variable $R'''
		return self._instance.R

	@property
	def tool_num(self) -> int:
		'''Value of variable $TOOL_NUM'''
		return self._instance.ToolNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UserToolVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
