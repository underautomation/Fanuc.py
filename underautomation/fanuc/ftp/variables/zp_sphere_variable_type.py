import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ZpSphereVariableType as zp_sphere_variable_type

class ZpSphereVariableType(GenericVariableType):
	'''Describes the Fanuc type ZP_SPHERE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zp_sphere_variable_type()
		else:
			self._instance = _internal

	@property
	def radius(self) -> float:
		'''Value of variable $RADIUS'''
		return self._instance.Radius

	@property
	def prog_name(self) -> typing.List[str]:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def line_num(self) -> typing.List[int]:
		'''Value of variable $LINE_NUM'''
		return self._instance.LineNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ZpSphereVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
