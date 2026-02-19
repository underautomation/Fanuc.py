import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbjopGrpVariableType as tbjop_grp_variable_type

class TbjopGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TBJOP_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbjop_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def f2mgn(self) -> float:
		'''Value of variable $F2MGN'''
		return self._instance.F2mgn

	@property
	def minf2(self) -> float:
		'''Value of variable $MINF2'''
		return self._instance.Minf2

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbjopGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
