import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GrsmtGrpVariableType as grsmt_grp_variable_type

class GrsmtGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type GRSMT_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = grsmt_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def grv_sw(self) -> int:
		'''Value of variable $GRV_SW'''
		return self._instance.GrvSw

	@property
	def grv_param(self) -> float:
		'''Value of variable $GRV_PARAM'''
		return self._instance.GrvParam

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GrsmtGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
